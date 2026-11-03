#!/usr/bin/env python3
"""Download pinned upstream tools without installing or running them (stdlib only)."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "catalog" / "tools.json"
GROUPS = {
    "audio": {"audio"},
    "play": {"audio", "play"},
    "author": {"author"},
    "dev": {"dev"},
    "all": {"audio", "play", "author", "dev"},
}
MAX_BYTES = 512 * 1024 * 1024
DOWNLOAD_HOSTS = {"github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com"}


class DownloadError(Exception):
    """A manifest, response, or existing file cannot be trusted for this download."""


def validate_tool(tool):
    for field in ("id", "version", "asset"):
        value = tool.get(field)
        if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", value):
            raise DownloadError(f"Campo {field} inválido: {value!r}")
    url = urllib.parse.urlsplit(tool.get("download_url", ""))
    if (url.scheme != "https" or url.hostname != "github.com" or url.username
            or url.password or url.port not in (None, 443) or url.query or url.fragment):
        raise DownloadError("La URL inicial debe ser una descarga HTTPS pública de GitHub")
    repo = tool.get("repository", "")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise DownloadError("Repositorio inválido")
    expected_path = f"/{repo}/releases/download/{tool['version']}/{tool['asset']}"
    if urllib.parse.unquote(url.path) != expected_path:
        raise DownloadError("URL distinta del repositorio, versión o asset declarados")
    if tool.get("group") not in GROUPS["all"]:
        raise DownloadError("Grupo desconocido")
    size = tool.get("size")
    if type(size) is not int or not 0 < size <= MAX_BYTES:
        raise DownloadError("Tamaño esperado fuera de rango")
    digest = tool.get("sha256")
    if digest is not None and not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise DownloadError("SHA-256 inválido")


def load_tools(path=MANIFEST):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not isinstance(data.get("tools"), list):
        raise DownloadError("Formato de manifiesto no soportado")
    seen = set()
    for tool in data["tools"]:
        validate_tool(tool)
        if tool["id"] in seen:
            raise DownloadError("ID duplicado")
        seen.add(tool["id"])
    return data["tools"]


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class OfficialRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        url = urllib.parse.urlsplit(newurl)
        if (url.scheme != "https" or url.hostname not in DOWNLOAD_HOSTS
                or url.username or url.password or url.port not in (None, 443)):
            raise DownloadError("Redirección fuera de los hosts de descarga permitidos")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def open_official(request, timeout=45):
    return urllib.request.build_opener(OfficialRedirects()).open(request, timeout=timeout)


def fetch_tool(tool, destination, opener=open_official):
    validate_tool(tool)
    base = Path(destination).expanduser().resolve()
    directory = base / tool["id"] / tool["version"]
    directory.mkdir(parents=True, exist_ok=True)
    if not directory.resolve().is_relative_to(base):
        raise DownloadError("La carpeta de destino sale de la raíz mediante un enlace")
    target = directory / tool["asset"]
    if target.is_symlink():
        raise DownloadError("El destino es un enlace simbólico")
    if target.exists():
        if (tool["sha256"] and target.is_file() and target.stat().st_size == tool["size"]
                and sha256_file(target) == tool["sha256"]):
            return {"status": "reused", "path": str(target), "upstream_hash_verified": True}
        raise DownloadError(f"No sobrescribo un archivo existente sin verificar: {target}")

    request = urllib.request.Request(tool["download_url"], headers={"User-Agent": "rocksmith-lab/1.0"})
    temp_path = None
    receipt_path = target.with_name(target.name + ".receipt.json")
    if receipt_path.exists() or receipt_path.is_symlink():
        raise DownloadError(f"Ya existe un recibo; revisar o elegir otro destino: {receipt_path}")
    try:
        with opener(request, timeout=45) as response:
            if response.status != 200:
                raise DownloadError(f"HTTP inesperado: {response.status}")
            kind = response.headers.get("Content-Type", "").lower()
            if any(t in kind for t in ("text/", "json", "xml")):
                raise DownloadError("El servidor devolvió una página o metadatos en lugar del binario")
            header_size = response.headers.get("Content-Length")
            if header_size is not None and int(header_size) != tool["size"]:
                raise DownloadError("Content-Length distinto del tamaño fijado")
            digest = hashlib.sha256()
            count = 0
            with tempfile.NamedTemporaryFile(dir=directory, prefix=".partial-", delete=False) as stream:
                temp_path = Path(stream.name)
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    if count == 0 and chunk.lstrip().lower().startswith((b"<!doctype html", b"<html", b"{", b"[")):
                        raise DownloadError("Respuesta de texto inesperada")
                    count += len(chunk)
                    if count > tool["size"]:
                        raise DownloadError("Descarga mayor que el tamaño fijado")
                    digest.update(chunk)
                    stream.write(chunk)
        if count != tool["size"]:
            raise DownloadError("Descarga incompleta")
        actual_hash = digest.hexdigest()
        if tool["sha256"] and actual_hash != tool["sha256"]:
            raise DownloadError("SHA-256 distinto del digest publicado")
        receipt = {
            "id": tool["id"], "version": tool["version"], "source_url": tool["download_url"],
            "downloaded_at": datetime.now(timezone.utc).isoformat(), "bytes": count,
            "sha256_calculated": actual_hash, "sha256_upstream": tool["sha256"],
            "upstream_hash_verified": tool["sha256"] is not None,
        }
        # Hard-link promotion is atomic and refuses to replace a destination created meanwhile.
        os.link(temp_path, target)
        try:
            with receipt_path.open("x", encoding="utf-8") as stream:
                json.dump(receipt, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
        except Exception:
            target.unlink()
            raise
        return {"status": "downloaded", "path": str(target), **receipt}
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="Listar versiones fijadas sin red")
    download = sub.add_parser("download", help="Descargar sin instalar ni ejecutar")
    download.add_argument("--group", choices=GROUPS, default="audio")
    download.add_argument("--dest", type=Path, default=ROOT / ".downloads")
    args = parser.parse_args(argv)
    try:
        tools = load_tools()
        if args.command == "list":
            for tool in tools:
                check = "SHA-256 publicado" if tool["sha256"] else "sin SHA-256 publicado"
                print(f"{tool['id']:20} {tool['version']:40} {tool['size']:>10} bytes  {check}")
            return 0
        selected = [t for t in tools if t["group"] in GROUPS[args.group]]
        for tool in selected:
            print(f"Descargando/verificando {tool['id']} {tool['version']}…", flush=True)
            result = fetch_tool(tool, args.dest)
            print(json.dumps(result, ensure_ascii=False), flush=True)
        return 0
    except (DownloadError, OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
