# Qué adaptar para un modo de aprendizaje divertido

Investigación del 2026-11-02. Objetivo: canciones favoritas y retos cortos de técnica y ritmo, con el mínimo de teoría necesaria. Todavía no se ha implementado un mod ni probado una integración en Linux.

## Piezas que ya existen

| Proyecto | Evidencia revisada | Qué aprovecharíamos | Qué falta comprobar |
| --- | --- | --- | --- |
| [RSMods](https://github.com/Lovrom8/RSMods) | README de develop: bucles, rebobinado, velocidad lineal de Riff Repeater, listas y guía Wine/Proton. | Herramientas de práctica dentro del juego, sin rehacerlas. | Funciones concretas de la release instalada y convivencia con las otras DLL. |
| [rs-manager](https://github.com/sandiz/rs-manager) | Readme.md, package.json y LICENSE: biblioteca, listas, estadísticas y RockSniffer; React/Electron; GPL-3.0. | Referencia para biblioteca, filtros e historial; estudiar sus módulos de integración. | Publica Windows/Mac; no declara un paquete Linux listo. El manifiesto mantiene Electron 7/React 16 y dependencias antiguas: portarlo tiene trabajo. |
| [RockSniffer](https://github.com/kokolihapihvi/RockSniffer) y [RockSnifferLib](https://github.com/kokolihapihvi/RockSnifferLib) | Estado y estadísticas en tiempo real; biblioteca C#/.NET 8 con licencia MIT. | Probar un adaptador de lectura de canción/arreglo y eventos de sesión. | Acceso al proceso y resultados correctos bajo Proton; distinguir resultado del intento y mejor marca histórica. |
| [Rocksmith2014.NET / DLC Builder](https://github.com/iminashi/Rocksmith2014.NET) | Biblioteca y herramientas de formatos ya investigadas. | Metadatos de arreglos; más adelante, ejercicios cortos propios si aportan algo. | Seleccionar API y validar con un PSARC local. |

RSMods no mostró un archivo de licencia en la raíz consultada. La ruta inicial consiste en usarlo como herramienta separada y revisar las condiciones del código concreto antes de copiar módulos. La inspección de licencias aquí registra archivos encontrados; no sustituye una revisión al decidir distribuir un fork.

## Decisión provisional

Un acompañante local pequeño puede añadir la guía que falta: elegir canción, recomendar un reto, abrir un recurso gratuito y conservar progreso. RSMods se encarga de funciones que ya implementa dentro del juego.

No hemos elegido un fork definitivo. rs-manager es el candidato más cercano por funciones, pero un port completo puede costar más que una capa pequeña. Primero probar la integración de lectura; después decidir con evidencia. No instalar dependencias de esos proyectos ni modificar el perfil del juego para esta investigación.

## Progresión que encaja con el usuario

1. Elegir una canción favorita o un fragmento motivador.
2. Mostrar un único objetivo: dedos, púa, silencio, pulso o continuidad.
3. Enlazar un recurso breve si hace falta.
4. Tocar y registrar el intento o una autoevaluación clara.
5. Recomendar el siguiente reto y dar una insignia opcional, conservando práctica libre.

El catálogo [missions.example.json](../catalog/missions.example.json) es un ejemplo editable de esta secuencia. No contiene una campaña ejecutable ni canciones descargadas.

## Datos automáticos y manuales

| Dato | Fuente prevista |
| --- | --- |
| Canción/arreglo actual y resultado del intento | RockSniffer, solo si la prueba bajo Proton funciona. |
| Dedos o púa utilizada | Elección manual: el juego no nos ofrece una identificación fiable de esta técnica. |
| Limpieza, tensión y si el fragmento suena bien | Autoescucha y autoevaluación. No fingir que un porcentaje lo demuestra. |
| Precisión rítmica en milisegundos | Fuera del primer prototipo. Requeriría analizar audio y compensar latencia, además de validar el método. |

Una métrica de aciertos puede informar, pero no certifica groove. Podemos dar progreso por completar un reto o practicar una habilidad sin convertir una medida insuficiente en examen.

## Primera prueba técnica

Mantener el experimento de [MODO_CARRERA.md](MODO_CARRERA.md): identificar tres intentos reales —completado, abandonado y repetido— con su arreglo, sin escribir perfiles. Guardar eventos de lectura y documentar límites antes de construir la interfaz.

Fuentes técnicas: README y archivos de los proyectos enlazados, consultados en la fecha indicada. La rama develop de RSMods puede contener funciones aún no incluidas en nuestra release fijada.
