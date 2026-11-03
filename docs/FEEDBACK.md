# fee[dB]ack: candidato para práctica guiada y plugins propios

Investigación documental del 2026-11-02 a partir de los enlaces del usuario. No se ha instalado ni probado con la UM2.

## Por qué merece una prueba

[fee[dB]ack](https://got-feedback.org/) es una plataforma musical abierta, antes llamada Slopsmith. La web presenta bajo, entrada por interfaz de audio, edición/importación de arreglos y extensiones. La organización declara AGPL-3.0 para el núcleo.

Para nuestro objetivo, el interés es reutilizar una plataforma extensible con práctica de bajo y resultados, y añadir una ruta pequeña basada en canciones favoritas.

## Piezas relevantes

| Pieza | Qué documenta | Uso posible |
| --- | --- | --- |
| [Virtuoso](https://github.com/got-feedBack/feedBack-plugin-virtuoso) | Rutinas secuenciadas, bases de bajo, ritmo, acompañamiento, sesiones y progreso opcional. El README actual describe indicadores de tendencia temporal y ayudas de dedos/púa. | Probar primero una rutina sencilla de bajo y otra rítmica; aprovechar su progresión antes de escribir una nueva. |
| [Note Detection](https://github.com/got-feedBack/feedBack-plugin-notedetect) | Selección de dispositivo/canal, detección de notas y eventos de acierto, fallo y sesión con diagnósticos de tiempo/afinación. | Verificar si sus resultados sirven para retos; no equivalen por sí solos a una valoración musical completa. |
| [Practice Journal](https://github.com/got-feedBack/feedBack-plugin-practice) | Tiempo, arreglo, velocidad y bucles usados por sesión. | Historial de práctica existente. |
| [Plugin specification](https://github.com/got-feedBack/feedBack-plugin-spec) | Manifiesto plugin.json, pantallas, ajustes y rutas; ejemplos y validador. | Añadir un plugin de guía, evitando modificar el núcleo como primer paso. |

La especificación admite JavaScript y rutas Python. La documentación del detector incluye eventos como `notedetect:session` y `note:hit`, útiles para un experimento de integración. Las versiones inspeccionadas mezclan nombres feedBack/Slopsmith en algunas APIs: comprobar el contrato del host instalado.

## Linux y estado de las descargas

La API de releases consultada devuelve estas opciones de escritorio:

| Versión/canal | Estado descrito | Linux |
| --- | --- | --- |
| v0.3.0-alpha.1 | Alpha, publicada el 2026-07-03 | AppImage y deb |
| nightly | Build nightly.20260722, publicada el 2026-07-23; su descripción la llama el canal menos estable | AppImage y deb, actualización manual |

[Releases oficiales](https://github.com/got-feedBack/feedBack-desktop/releases).

No llamar estable a una alpha porque el campo GitHub prerelease sea false. La web ofrece nightly y la presentación de la organización aún menciona preparar el primer lanzamiento; los artefactos publicados dan una evidencia más concreta.

El README actual de Virtuoso contiene apartados de funciones hasta v0.7.23, pero el plugin.json leído declara 0.2.6. Esto no prueba que falte el código; impide asumir que la numeración del README coincide con lo incluido en un instalador. Fijar host y plugin al ensayar.

## Canciones favoritas y CDLC

La web documenta Guitar Pro, MusicXML y feedpak. No damos por verificada la carga directa de nuestros PSARC.

Existe un proyecto independiente, [psarc2feedpak](https://github.com/carelesshangman/psarc2feedpak), que documenta conversión de notas, arreglos y audio. Su paquete preparado se centra en Windows; desde código menciona Python, ffmpeg y vgmstream. La ejecución Linux y el resultado de un archivo concreto siguen pendientes.

Primero probar contenido de ejemplo o un arreglo propio sencillo. Después, si interesa reutilizar CDLC locales, verificar un solo archivo: presencia del arreglo Bass, sincronía, técnicas y dificultad. No incorporar canciones o paquetes convertidos al repositorio.

## Evaluación propuesta: una sesión, antes de desarrollar

1. Abrir una build Linux oficial y anotar versión de host y plugins.
2. Seleccionar UM2 y la entrada donde realmente llega INST 2; comprobar la señal limpia y la escucha.
3. Probar notas lentas, especialmente Mi grave, y después una figura repetida a un tempo cómodo.
4. Escuchar si hay retraso perceptible y comparar la respuesta con lo tocado. No usar una puntuación para concluir que una mala calibración es un error del músico.
5. Ejecutar una rutina básica de Virtuoso y comprobar si su pantalla resulta clara y divertida.
6. Observar eventos de un intento terminado, uno abandonado y uno repetido. Revisar resultados y persistencia.
7. Solo después, probar una canción propia o un archivo convertido y decidir qué plataforma usar.

La documentación del detector explica la relación entre tamaño de ventana y notas graves. Ese buffer no debe confundirse con el buffer de salida de RS ASIO: son rutas y medidas diferentes. No hay todavía una configuración UM2 validada aquí.

## Decisión provisional para el proyecto

**Actualización del 2026-11-03:** la ruta principal de aprendizaje es Rocksmith 2014 con favoritas y guía corta; ver [decisión y experiencias](EXPERIENCIAS_REDDIT.md). fee[dB]ack queda como alternativa y experimento técnico posterior. Si su audio, detector y contenido funcionan bien, un plugin pequeño podría presentar nuestra ruta, enlazar recursos y sugerir retos entre canciones favoritas, reutilizando Virtuoso y el historial existentes.

El complemento mostraría un paso actual y Continuar, mantendría las canciones disponibles y conservaría los datos personales localmente. Dedos/púa usados seguirían siendo una elección manual: mostrar letras o golpes sugeridos no demuestra reconocer cómo toca la persona.

No se abandona Rocksmith por una página promocional. La elección se hará con la prueba de uso. Para la ruta Rocksmith sigue pendiente validar RockSniffer; para fee[dB]ack, validar sus propios eventos.

Antes de desarrollar interfaz, resolver esas pruebas. No se ha creado un plugin ni instalado software como parte de esta investigación.

## Fuentes primarias

- Web y descargas: https://got-feedback.org/
- Organización y núcleo: https://github.com/got-feedBack
- Releases: https://github.com/got-feedBack/feedBack-desktop/releases
- Virtuoso y manifiesto: https://github.com/got-feedBack/feedBack-plugin-virtuoso
- Detector: https://github.com/got-feedBack/feedBack-plugin-notedetect
- Historial: https://github.com/got-feedBack/feedBack-plugin-practice
- Especificación: https://github.com/got-feedBack/feedBack-plugin-spec
- Conversor independiente: https://github.com/carelesshangman/psarc2feedpak
- Diagnóstico del detector: https://github.com/got-feedBack/feedBack/blob/main/docs/note-detect-tuning.md
