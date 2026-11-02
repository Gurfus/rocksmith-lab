# Trabajo en este repositorio

El objetivo es Rocksmith 2014 Remastered en Linux con UM2, CDLC de bajo y una futura carrera local. La documentación está en español.

- Distinguir evidencia documental, datos declarados y pruebas reales. No afirmar compatibilidad bajo Proton sin comprobarla.
- Mantener fuentes primarias y fecha de consulta. Separar experiencias de usuarios de requisitos oficiales.
- No añadir música, PSARC, DLL, EXE, AppImage, datos de Steam, perfiles ni credenciales a Git.
- No ejecutar instaladores ni modificar el juego como parte de descargar herramientas. Los cambios de configuración necesitan copia y prueba en el equipo objetivo.
- Los digests calculados localmente no equivalen a digests publicados por el autor o la plataforma.
- Evitar construir la UI de la carrera antes de validar audio y lectura de intentos: RockSniffer bajo Proton para la ruta Rocksmith, o eventos del host si se evalúa fee[dB]ack.
- Para cambios del descargador: ejecutar `python3 -m unittest discover -s tests -v` y una lista del manifiesto. Probar casos de integridad y preservación de archivos.
