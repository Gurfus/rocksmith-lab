# Audio Bridge, QuickRS y práctica eficiente

Revisión del 2026-11-02 de los tres enlaces aportados por el usuario. Investigación de documentación y código, sin instalar, compilar ni ensayar con la UM2.

## Decisión para no dispersarnos

| Proyecto | Qué aporta a nuestro objetivo | Situación para Linux + bajo |
| --- | --- | --- |
| Rocksmith Audio Bridge | Mejoras dentro de Rocksmith, grabación, transposición y práctica nota a nota. Incluye RSMods. | Requisitos publicados de Windows; no se ha verificado bajo Proton. Bajo experimental en Note by Note. No añadirlo como requisito inicial. |
| QuickRS 0.3.0 | Reproductor autónomo, bucles y revisión de una pasada por notas y compases. Código Rust/MIT. | Descargas publicadas para Windows/macOS. El código contempla un backend de sistema mediante CPAL para Linux, pero no se ha compilado ni probado aquí. El autor reconoce carencias en bajo. |
| fee[dB]ack + Virtuoso | Plataforma extensible y práctica progresiva de bajo/ritmo. | Alternativa nativa para una prueba posterior, según [la evaluación previa](FEEDBACK.md); audio y resultados pendientes de validar. |

Actualización del 2026-11-03: [Rocksmith 2014 con favoritas y guía corta](EXPERIENCIAS_REDDIT.md) es la ruta principal de aprendizaje. Estas herramientas se conservan como mejoras opcionales, alternativas o candidatos de desarrollo.

No sumar estas herramientas como instalaciones obligatorias. Para aprender se conserva la [ruta inicial](RUTA_INICIAL.md). Para desarrollo, probar una base y un resultado real antes de escribir una interfaz.

## Rocksmith Audio Bridge

Es un fork/extensión de RSMods, antes llamado RSModsPlus. El README documenta un puente de audio, transposición, grabación, mezcla y un host VST3. Su instalador incluye RSMods y componentes de Windows; no se deben apilar instaladores sin revisar qué sustituyen.

Puede usar una interfaz ASIO a través de RS ASIO; no exige un Real Tone Cable. Eso no acredita que su puente funcione con UM2 y Proton.

La release **v4.3.0-beta.1**, publicada el 2026-10-19, añade soporte de Learn & Play y drivers ASIO de 64 bits. No confundir la versión del mod con la edición o compilación del juego.

**Note by Note** ofrece espera en cada nota o avance mientras se acierta. El propio proyecto califica de experimental el soporte de bajo. Propuesta nuestra: usarlo para descifrar un pasaje y luego repetirlo sin interrupciones para practicar ritmo. Pausar al fallar y sostener el pulso son tareas diferentes.

Fuentes: [README](https://github.com/Cheesewizard/RocksmithAudioBridge), [release beta](https://github.com/Cheesewizard/RocksmithAudioBridge/releases/tag/v4.3.0-beta.1).

## Qué dice realmente el primer hilo de Reddit

[Getting the most out of Rocksmith 2014 Remastered](https://www.reddit.com/r/rocksmith/comments/1xjawld/getting_the_most_out_of_rocksmith_2014_remastered/).

La página y el JSON no devolvieron el contenido en nuestra consulta; el [RSS](https://www.reddit.com/r/rocksmith/comments/1xjawld/getting_the_most_out_of_rocksmith_2014_remastered/.rss) sí permitió leer 20 entradas.

- El autor de Audio Bridge recomienda su fork y enlaza la beta compatible con Learn & Play.
- Un usuario describe que Note by Note no conserva su activación con 4.2 y dice resolverlo al actualizar. Es una experiencia concreta, no una garantía.
- La conversación sobre Avalonia y un futuro port de RSMods a Mac habla de desarrollo pendiente. No demuestra soporte Linux actual.
- Se mencionan un overlay de tablaturas y una guía de práctica.

El [overlay](https://github.com/GrzegorzAndrys/rocksmith-tab-overlay) usa RockSniffer para seguir la canción; su README pide Windows 10/11 y runtime de escritorio .NET. Se registra como referencia visual, sin añadirlo a la ruta Linux.

## QuickRS: la pieza más interesante para estudiar el ritmo

[Repositorio](https://github.com/arpan2711/quickRS-player). La release **0.3.0** se publicó el **2026-10-29**, con paquetes Windows y macOS.

El README documenta bucles, cambios de velocidad, tablatura/highway y dos acciones distintas:

- **Take:** grabar una pasada de un fragmento y contrastarla con el arreglo.
- **Recording:** guardar lo que se oye, sin que eso implique evaluarlo.

La [guía de reproducción](https://github.com/arpan2711/quickRS-player/blob/main/docs/PLAYING.md) describe resultados por compás, notas correctas/erróneas y tendencia temporal. El análisis es local. No se ha medido su precisión con bajo.

### Lo comprobado en código

- [Cargo.toml](https://github.com/arpan2711/quickRS-player/blob/main/Cargo.toml): workspace Rust y licencia MIT.
- [backend/system.rs](https://github.com/arpan2711/quickRS-player/blob/main/crates/qrs-audio/src/backend/system.rs): backend CPAL; el comentario contempla ALSA/PulseAudio en Linux. Eso es una pista de portabilidad, no una prueba de compilación o funcionamiento.
- [pitch.rs](https://github.com/arpan2711/quickRS-player/blob/main/crates/qrs-analysis/src/pitch.rs): existe una prueba sintética con una frecuencia de 41,2 Hz. No corresponde afirmar que el proyecto carece totalmente de soporte de graves; tampoco equivale a validar una toma real.
- [take_cmd.rs](https://github.com/arpan2711/quickRS-player/blob/main/crates/qrs-cli/src/take_cmd.rs): CLI para analizar una grabación contra un arreglo, con parámetros de velocidad/offset y salida JSON. Puede ser una integración útil para nuestro proyecto.
- [take.rs](https://github.com/arpan2711/quickRS-player/blob/main/crates/qrs-analysis/src/take.rs): el analizador compara ataques y notas con el arreglo y separa alineación y resultados temporales. La calibración importa antes de atribuir todo desfase al intérprete.

### El límite que destaca el autor

En el [hilo de QuickRS 0.3.0](https://www.reddit.com/r/rocksmith/comments/1xixj45/quickrs_030_the_free_rs2014_practice_player_now/), el autor reconoce huecos en la compatibilidad con bajo y aspectos por mejorar de la interfaz. Es evidencia sobre su estado, no un benchmark.

La versión actual documenta PSARC y feedpak. Los mensajes antiguos de 0.1.0 que describen solo feedpak no deben sustituir las instrucciones actuales. No se incluyen ni se publicarán canciones, claves o grabaciones privadas en este repositorio.

## Cómo podría adaptarse al futuro proyecto

Propuesta propia: si la prueba nativa resulta viable, usar la CLI o estudiar qrs-analysis para obtener un informe local y convertirlo en un reto comprensible: repetir un compás, escuchar su pausa o mantener el pulso al cambiar de nota.

Antes de adoptarlo:

1. Comprobar una compilación de Linux y enumeración de la UM2.
2. Ensayar un fragmento sencillo de bajo, con un offset de audio comprobado.
3. Comparar una pasada estable, otra deliberadamente adelantada/retrasada y una con errores de nota.
4. Revisar el JSON y verificar que distingue esas situaciones de forma útil.
5. Decidir si reutilizar la CLI, colaborar con el proyecto o conservar otra plataforma.

No hay todavía un port ni un adaptador implementado.

## Guía de práctica enlazada en el hilo

La [guía histórica de Rocksmith eficiente](https://www.reddit.com/r/rocksmith/comments/4529dt/a_guide_how_to_use_rocksmith_efficiently_also/) se leyó por RSS. Es una propuesta de un usuario con experiencia, no un currículo oficial.

Recomienda trabajar fragmentos lentos, conservar las notas del pasaje y escuchar lo tocado; también distingue aprendizaje de posiciones y práctica de tiempo. Para este usuario conservamos esa idea en pasajes asequibles, sin imponer todas las notas de un tema imposible ni convertirlo en una rutina pesada.

## Fuentes y límites

Todos los enlaces anteriores son páginas del proyecto, código o experiencias de sus autores/usuarios. Las afirmaciones de funcionamiento son documentales. No se han ejecutado instaladores, compilado QuickRS ni validado detección o latencia en el equipo del usuario.
