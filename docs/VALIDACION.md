# Validación del repositorio

Fecha: 2026-11-02. Entorno de preparación remoto, distinto del ordenador donde se jugará.

- Nueve pruebas unitarias correctas: integridad SHA-256, tamaño, respuestas HTML, preservación de archivos existentes, reutilización verificada, rutas del manifiesto y ausencia de digest publicado.
- El manifiesto se carga y lista sin acceso a la red.
- Descarga real completada de los cinco paquetes mediante el script incluido. Tamaños coincidentes: 168.444.503 bytes en total.
- Los SHA-256 de RS ASIO, PipeASIO Manager, RSMods y DLC Builder coinciden con los digests publicados por GitHub y fijados en el manifiesto.
- RockSniffer coincide en tamaño. SHA-256 calculado localmente: `e1f0a215eea3843b573a7163acb094e80d7a3653077f6b230d342f248fc70186`. No había digest publicado con el que contrastarlo.
- Los binarios y recibos están en la carpeta ignorada `.downloads/`; no forman parte del repositorio.

No se han ejecutado esos binarios ni instalado componentes. No se han probado el juego, la UM2, los CDLC ni la lectura de resultados bajo Proton en el ordenador del usuario. Las pruebas del descargador no demuestran compatibilidad musical o de audio.
