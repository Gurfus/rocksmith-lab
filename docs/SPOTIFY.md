# Spotify como fuente de repertorio

Decisión anotada el 2026-11-02: partir de la música que ya escucha el usuario para elegir canciones de bajo y alimentar la futura guía de retos.

## Primero: un volcado con Exportify

Usar [Exportify](https://exportify.app/). Su documentación describe acceso de solo lectura y exportación de playlists, Liked Songs y álbumes guardados a CSV. “Export All” genera un ZIP con los archivos.

El primer paso pendiente es exportar favoritas o una playlist representativa e importar sus metadatos: título, artista, álbum, URI/enlace de Spotify e ISRC cuando esté disponible. Después deduplicar versiones y buscar qué temas tienen un arreglo de bajo utilizable en Rocksmith/CDLC. Revisar dificultad y afinación del arreglo real; no inferirlas solo del BPM o del género.

La herramienta no se ha probado con la cuenta del usuario y todavía no existe un importador en este repositorio.

## Después: valorar un MCP local

[gupta-kush/spotify-mcp](https://github.com/gupta-kush/spotify-mcp) documenta sincronización de favoritas y playlists creadas por el usuario a un índice JSON local, además de búsquedas sobre ese índice. Es un candidato por evaluar, no una dependencia adoptada o instalada.

Una aplicación propia en Development Mode requiere actualmente que su propietario tenga Spotify Premium. Hay límites de usuarios y de acceso a playlists; comprobar las reglas vigentes al configurarla. Para el primer volcado no necesitamos montar este MCP.

## Encaje con el futuro mod

Repertorio personal → coincidencias con arreglos locales/CDLC → revisión de instrumento, afinación y dificultad → canciones sugeridas para la ruta de aprendizaje.

El acompañante podría recordar “quiero aprender estas canciones” y recomendar un siguiente reto entre ellas. La importación de metadatos, la búsqueda de arreglos y la evaluación musical son pasos distintos; ninguno está automatizado todavía.

## Datos personales fuera del repositorio público

Guardar los CSV, JSON, índices y credenciales solo localmente. Ruta prevista para el volcado: `local/spotify/`; `local/` ya está excluida de Git. Publicar únicamente el código, documentación y ejemplos ficticios que desarrollemos.

Estado: idea documentada; ninguna cuenta conectada ni biblioteca importada.

Fuentes consultadas el 2026-11-02:

- Exportify, funciones y permisos: https://github.com/watsonbox/exportify/blob/master/README.md
- MCP candidato: https://github.com/gupta-kush/spotify-mcp
- Spotify, modos y requisito Premium: https://developer.spotify.com/documentation/web-api/concepts/quota-modes
- Alternativa oficial de descarga de datos JSON: https://support.spotify.com/es/article/understanding-your-data/
