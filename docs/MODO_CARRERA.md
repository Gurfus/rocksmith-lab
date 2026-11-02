# Propuesta: una carrera con canciones favoritas

**Idea del usuario:** jugar canciones custom de los grupos que le gustan, con una progresión parecida a Guitar Hero: niveles, dificultad gradual, estrellas y desbloqueos. Es una propuesta para construir; aún no hay un mod funcional aquí.

## Lo que ya existe

- El Rocksmith original tenía Journey. Rocksmith 2014 ofrece otras actividades, incluido Score Attack; no equivale a aquella campaña.
- El campeonato de CustomsForge aporta dificultad humana por instrumento y comparación de resultados.
- rs-manager ya ofrece biblioteca, listas y seguimiento. RockSniffer proporciona una posible base de lectura del juego.

No hemos identificado un producto terminado que reúna esta carrera, CDLC propios seleccionados y Linux. Hay que probar esas piezas antes de decidir si conviene extender un proyecto existente o crear un acompañante.

## Primera versión que tendría sentido

Aplicación local acompañante, inicialmente centrada en bajo. Importar unos **20 CDLC locales**, con dificultad y afinación revisadas manualmente, y agruparlos en cuatro capítulos: ensayo, primer bolo, gira y festival. Mantener un modo de práctica libre junto a los desbloqueos.

Ejemplo de regla **a probar**, no una exigencia musical validada: desbloquear el capítulo siguiente al superar 3 de 5 canciones con al menos 85 % en condiciones comparables. Las estrellas y los jefes de capítulo pueden venir después. No premiar simplemente tocar muchas veces un arreglo simplificado.

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
