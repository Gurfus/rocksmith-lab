# Rocksmith Lab

Investigación y preparación de **Rocksmith 2014 Remastered en Linux**, con **Behringer U-Phoria UM2**, canciones custom y un posible modo carrera con progresión tipo Guitar Hero.

Estado: **2 de noviembre de 2026**. Hay documentación, un descargador y una propuesta de desarrollo. La integración con el juego y el audio en el equipo del usuario siguen pendientes de prueba.

## Empezar

Requisitos del descargador: Python 3.10 o posterior y acceso a Internet. No necesita dependencias de pip.

```bash
git clone https://github.com/Gurfus/rocksmith-lab.git
cd rocksmith-lab
python3 scripts/fetch_tools.py list
python3 scripts/fetch_tools.py download --group audio
```

Las descargas quedan en `.downloads/`. El script comprueba tamaños y los SHA-256 disponibles; no ejecuta instaladores ni cambia archivos del juego.

| Quiero… | Leer / ejecutar |
| --- | --- |
| Entender licencias, ediciones, mods y Rocksmith+ | [Investigación completa](docs/INVESTIGACION.md) |
| Conectar la UM2 y configurar Linux | [Guía Linux + UM2](docs/LINUX_UM2.md) |
| Saber qué descargar y en qué orden | [Descargas](docs/DESCARGAS.md) |
| Encontrar CDLC y herramientas de creación | [Comunidad](docs/COMUNIDAD.md) |
| Seguir un orden corto y saber qué hacer ahora | [Ruta inicial](docs/RUTA_INICIAL.md) |
| Usar mis favoritas de Spotify como repertorio | [Volcado de Spotify y futuro MCP](docs/SPOTIFY.md) |
| Aprender con recursos gratis, canciones y poca teoría | [Aprender jugando](docs/APRENDER_JUGANDO.md) |
| Diseñar la carrera con canciones favoritas | [Modo carrera](docs/MODO_CARRERA.md) |
| Elegir proyectos que adaptar y retos para la carrera | [Adaptar mods](docs/ADAPTAR_MODS.md) |
| Ver qué está confirmado y qué falta | [Estado](docs/ESTADO.md) y [roadmap](ROADMAP.md) |
| Consultar las fuentes | [SOURCES.md](SOURCES.md) |

## Canciones custom

Se buscan en [CustomsForge / Ignition](https://ignition4.customsforge.com/) con cuenta gratuita, eligiendo arreglo **Bass** y archivo **`_p.psarc`** para el juego de Windows bajo Proton. El habilitador se descarga desde su página oficial; el procedimiento está en la guía.

El repositorio no incluye música, DLC oficiales, archivos del juego ni perfiles de Steam. Las canciones y los binarios descargados permanecen fuera de Git.

## Desarrollo

```bash
python3 -m unittest discover -s tests -v
```

El primer experimento del modo carrera será obtener un resultado de una canción terminada bajo Proton. La interfaz, los capítulos y los desbloqueos se construirán después de validar esa integración.
