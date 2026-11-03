# Descargar las herramientas

## Descargador incluido

```bash
python3 scripts/fetch_tools.py list
python3 scripts/fetch_tools.py download --group audio
python3 scripts/fetch_tools.py download --group play
python3 scripts/fetch_tools.py download --group author
python3 scripts/fetch_tools.py download --group dev
python3 scripts/fetch_tools.py download --group all
```

| Grupo | Contenido | Momento |
| --- | --- | --- |
| audio | RS ASIO + PipeASIO Manager | Primero: hacer funcionar la UM2. |
| play | audio + RSMods | Después de una canción base; RSMods es opcional. |
| author | DLC Builder Linux | Solo si queremos crear o modificar arreglos. |
| dev | RockSniffer | Prueba de integración del modo carrera. |
| all | Todos los anteriores | Preparar material, sin instalarlo. |

El manifiesto fija las versiones consultadas el 2026-11-02; no busca silenciosamente la última versión. Cada archivo se guarda bajo `.downloads/<id>/<version>/`, junto a un recibo JSON. Los hashes de cuatro paquetes proceden del digest publicado por GitHub. RockSniffer solo tiene tamaño esperado y hash calculado localmente: el recibo lo distingue.

Si un archivo existente coincide con el hash esperado, se reutiliza. Si no hay digest publicado o el archivo es distinto, se rechaza la sobrescritura; conviene revisar el archivo y usar otra carpeta con `--dest`. El script tampoco extrae ZIP, instala DLL, ejecuta EXE/AppImage ni acepta licencias.

## Descargas manuales

| Qué | Fuente y motivo |
| --- | --- |
| Juego | Steam → Biblioteca → Rocksmith 2014 Remastered, AppID 221680. Instalar la licencia propia. |
| CDLC Enabler | https://ignition4.customsforge.com/tools/cdlcenabler — página oficial, versión y guía vigentes. Su botón sirve un instalador de Windows. |
| Canciones | https://ignition4.customsforge.com/ — cuenta gratuita, selección manual por artista/arreglo/afinación. Descargar el archivo `_p.psarc`. |
| EOF | https://editoronfire.com/ — consultar la compilación actual. No fijamos un enlace de hotfix sin verificarlo. |
| Wwise | https://ignition4.customsforge.com/tools/wwise — elegir el paquete compatible con DLC Builder y revisar sus condiciones. |

Para tocar CDLC existentes no hacen falta EOF, Wwise ni DLC Builder. Las canciones no se descargan con este script. Revisar las reglas de CustomsForge: los DLC oficiales y el contenido incluido en el juego no se redistribuyen como CDLC, tampoco cuando se retiran de venta.

## Instalación posterior

Antes de instalar necesitamos distro, tipo de Steam, Proton y ruta del juego. PipeASIO Manager no soporta Steam Flatpak en la documentación consultada; no aplicar su receta directamente a ese entorno.

No ejecutar instaladores de Windows con el Wine global suponiendo que eso modifica el prefijo de Proton del juego. Hay que seleccionar y comprobar el prefijo correcto y seguir la documentación de cada herramienta. [LINUX_UM2.md](LINUX_UM2.md) define el orden de pruebas.
