# Propuesta: una carrera con canciones favoritas

**Idea del usuario:** jugar canciones custom de los grupos que le gustan, con una progresión parecida a Guitar Hero: niveles, dificultad gradual, estrellas y desbloqueos. Es una propuesta para construir; aún no hay un mod funcional aquí.

**Preferencias concretadas:** aprendizaje autodidacta, gratuito, divertido y basado en canciones; técnica de dedos y púa, ritmo y teoría solo cuando ayude. La progresión debe orientar sin impedir tocar favoritas. Recursos en [APRENDER_JUGANDO.md](APRENDER_JUGANDO.md) y opciones de integración en [ADAPTAR_MODS.md](ADAPTAR_MODS.md).

## Lo que ya existe

- El Rocksmith original tenía Journey. Rocksmith 2014 ofrece otras actividades, incluido Score Attack; no equivale a aquella campaña.
- El campeonato de CustomsForge aporta dificultad humana por instrumento y comparación de resultados.
- rs-manager ya ofrece biblioteca, listas y seguimiento. RockSniffer proporciona una posible base de lectura del juego.

No hemos identificado un producto terminado que reúna esta carrera, CDLC propios seleccionados y Linux. Hay que probar esas piezas antes de decidir si conviene extender un proyecto existente o crear un acompañante.

## Primera versión que tendría sentido

Aplicación local acompañante, inicialmente centrada en bajo. Empezar con unas pocas canciones favoritas y ampliar a una selección de unos **20 CDLC locales**, con dificultad y afinación revisadas manualmente. Los capítulos —ensayo, primer bolo, gira y festival— pueden organizar objetivos e insignias, manteniendo siempre disponibles las favoritas.

Los retos cortos de [missions.example.json](../catalog/missions.example.json) vinculan canción, técnica y recurso gratuito. No se fija un umbral universal del 85 % ni se equiparan aciertos y buen ritmo. Dedos/púa y calidad musical se registran por autoevaluación; los datos del juego solo se usan si están verificados. Insignias y recomendaciones son opcionales y no bloquean canciones.

Decisión del 2026-11-03: empezar con Rocksmith y ensayar manualmente tres favoritas antes de ampliar la campaña. El acompañante debe orientar qué practicar hoy y registrar continuidad, autoescucha del pulso e independencia visual como autoevaluaciones separadas del marcador. Las [experiencias de Reddit y sus límites](EXPERIENCIAS_REDDIT.md) explican este criterio.

## Datos mínimos

| Entidad | Campos |
| --- | --- |
| Canción/arreglo | ID local estable, artista, título, instrumento, afinación, identificador de arreglo, revisión/hash del archivo. |
| Dificultad | Valor humano, escala utilizada, procedencia, confianza, DD presente. |
| Intento | Canción y arreglo, fecha, modo, nivel de notas/DD, finalizado o abandonado, resultado, fuente y versión del lector. |
| Progreso | Reglas de campaña y versión, estrellas y desbloqueos derivados de intentos válidos. |

No subir PSARC, audio o perfiles al servidor. No escribir el perfil de Rocksmith para simular progreso. El acompañante conserva su propio historial local.

## Primer experimento: resultado fiable bajo Proton

1. Ejecutar RockSniffer con nuestra instalación y comprobar si detecta canción y arreglo de bajo.
2. Observar una canción completada, una abandonada y otra repetida.
3. Determinar qué campos se actualizan y si permiten distinguir el resultado del intento del mejor resultado histórico.
4. Guardar un evento de sesión sin escribir archivos del juego.
5. Documentar qué combinación de versiones funciona y qué campos faltan.

**Criterio de éxito:** identificar correctamente tres intentos, sus arreglos y su finalización; no contabilizar abandono como victoria ni repetir un resultado viejo. Hasta conseguirlo no prometemos puntuación automática. Si el lector no ofrece datos suficientes, se puede probar una campaña con confirmación manual, claramente indicada.

## Orden de implementación

1. Validación de lectura bajo Proton.
2. Inventario local de arreglos y lista curada de 20 canciones.
3. Modelo de intentos y reglas deterministas, sin depender de la UI.
4. Una pantalla de capítulos y progreso local.
5. Importación más cómoda, afinaciones y sugerencias de dificultad.

La dificultad automática necesitaría más que notas por segundo: técnicas, cruces de cuerda, posiciones, duración y resistencia. Empezar con valoración humana y usar heurísticas solo como ayuda. No hace falta transcribir MP3 ni crear todos los charts para empezar.

Fuentes y precedentes: [SOURCES.md](../SOURCES.md), sección carrera.
