import hashlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("fetch_tools", Path(__file__).resolve().parents[1] / "scripts/fetch_tools.py")
fetch = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fetch)
BODY = b"PK\x03\x04sample-tool-contents"


class Response(io.BytesIO):
    status = 200

    def __init__(self, body=BODY, headers=None):
        super().__init__(body)
        self.headers = headers if headers is not None else {"Content-Type": "application/octet-stream"}


class Downloads(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.tool = {
            "id": "example", "version": "v1", "asset": "example.zip", "group": "audio",
            "repository": "example/tool", "download_url": "https://github.com/example/tool/releases/download/v1/example.zip",
            "size": len(BODY), "sha256": hashlib.sha256(BODY).hexdigest(),
        }

    def opener(self, body=BODY, headers=None):
        return lambda request, timeout: Response(body, headers)

    def target(self):
        return self.root / "example/v1/example.zip"

    def assert_clean(self):
        self.assertFalse(self.target().exists())
        self.assertEqual(list(self.root.rglob(".partial-*")), [])

    def test_valid_download_and_verified_reuse_without_network(self):
        result = fetch.fetch_tool(self.tool, self.root, opener=self.opener())
        self.assertTrue(result["upstream_hash_verified"])
        self.assertEqual(self.target().read_bytes(), BODY)
        result = fetch.fetch_tool(self.tool, self.root, opener=lambda *a, **k: self.fail("network on reuse"))
        self.assertEqual(result["status"], "reused")

    def test_wrong_digest_cleans_partial_file(self):
        self.tool["sha256"] = "0" * 64
        with self.assertRaises(fetch.DownloadError):
            fetch.fetch_tool(self.tool, self.root, opener=self.opener())
        self.assert_clean()

    def test_short_and_oversized_body_are_rejected(self):
        for body in (BODY[:-1], BODY + b"extra"):
            with self.subTest(body=body), self.assertRaises(fetch.DownloadError):
                fetch.fetch_tool(self.tool, self.root, opener=self.opener(body))
            self.assert_clean()

    def test_existing_different_file_is_preserved(self):
        self.target().parent.mkdir(parents=True)
        self.target().write_bytes(b"keep me")
        with self.assertRaises(fetch.DownloadError):
            fetch.fetch_tool(self.tool, self.root, opener=lambda *a, **k: self.fail("network on conflict"))
        self.assertEqual(self.target().read_bytes(), b"keep me")

    def test_html_login_page_is_rejected_even_with_binary_content_type(self):
        for headers in ({"Content-Type": "text/html"}, {"Content-Type": "application/octet-stream"}):
            with self.subTest(headers=headers), self.assertRaises(fetch.DownloadError):
                fetch.fetch_tool(self.tool, self.root, opener=self.opener(b"<!doctype html>login", headers))
            self.assert_clean()

    def test_manifest_rejects_traversal_wrong_host_and_http(self):
        for changes in ({"asset": "../escape.zip"}, {"version": "../v1"},
                        {"download_url": self.tool["download_url"].replace("https:", "http:")},
                        {"download_url": self.tool["download_url"].replace("github.com", "example.com")},
                        {"repository": "different/repo"}):
            with self.subTest(changes=changes), self.assertRaises(fetch.DownloadError):
                fetch.validate_tool({**self.tool, **changes})

    def test_missing_upstream_digest_is_not_reported_as_verified(self):
        self.tool["sha256"] = None
        result = fetch.fetch_tool(self.tool, self.root, opener=self.opener())
        self.assertFalse(result["upstream_hash_verified"])
        self.assertEqual(result["sha256_calculated"], hashlib.sha256(BODY).hexdigest())
        with self.assertRaises(fetch.DownloadError):
            fetch.fetch_tool(self.tool, self.root, opener=self.opener())

    def test_content_length_mismatch_fails_before_writing(self):
        with self.assertRaises(fetch.DownloadError):
            fetch.fetch_tool(self.tool, self.root, opener=self.opener(headers={"Content-Length": "1"}))
        self.assert_clean()

    def test_repository_manifest_is_valid_and_ids_unique(self):
        tools = fetch.load_tools()
        self.assertEqual(len(tools), 5)
        self.assertEqual(len({t["id"] for t in tools}), len(tools))


if __name__ == "__main__":
    unittest.main()
