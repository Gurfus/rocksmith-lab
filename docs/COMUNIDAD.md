# Comunidad, canciones y herramientas

## Buscar canciones

[CustomsForge / Ignition](https://ignition4.customsforge.com/) concentra el catálogo comunitario. La cifra pública de registros no equivale a canciones únicas ni garantiza arreglo de bajo.

1. Crear o usar una cuenta gratuita y buscar el artista o título.
2. Filtrar por arreglo **Bass**, comprobar afinación, comentarios, revisión y dificultad dinámica.
3. Descargar la versión PC **`_p.psarc`**, también al jugar en Linux con Proton.
4. Seguir la guía vigente de CDLC Enabler y probar un archivo antes de llenar la carpeta `dlc`.

La guía moderna del habilitador no exige comprar Cherub Rock; muchas guías antiguas sí lo mencionan. El catálogo y las descargas requieren sus propios pasos de acceso; el repositorio no automatiza cuentas ni descargas masivas.

## Primeras búsquedas

Interesan Gloryhammer, Alestorm, Metallica y Red Hot Chili Peppers. El [taller de Teinashu](https://customsforge.com/topic/2937-teinashus-hall-of-glory/) documenta arreglos de temas de Gloryhammer y Alestorm. Eso no verifica hoy cada enlace, afinación o calidad del arreglo. No asignar dificultad sin revisarlo y tocarlo.

El [catálogo de ejemplo](../catalog/songs.example.json) contiene candidatos con campos pendientes; no es una colección descargada ni una clasificación validada.

## Qué aportan los proyectos existentes

| Proyecto | Uso | Límite relevante |
| --- | --- | --- |
| RSMods | Práctica, bucles, rebobinado, interfaz | Añadir funciones poco a poco; verificar compilación. |
| rs-manager | Biblioteca, listas, progreso, integración RockSniffer | Revisar antes de duplicar un gestor. |
| RockSniffer / RockSnifferLib | Lectura del estado y estadísticas | Resultado final y funcionamiento bajo Proton por comprobar. |
| DLC Builder / Rocksmith2014.NET | PSARC, SNG, XML, DD y empaquetado | Distribución Linux; Wwise puede requerir Wine. |
| EOF | Autoría de notas, técnicas y sincronía | Consultar distribución actual y flujo compatible. |
| psarcjs | Herramientas PSARC desde Node | Revisar dependencias antiguas antes de adoptarlo. |
| CFSM 2 | Nuevo gestor | Alfa Windows; Linux anunciado para después de 1.0. |

## Dificultad

El campeonato de CustomsForge usa niveles humanos por instrumento: **Beginner 1–3**, **Intermediate 4–5**, **Advanced 6–7**, **Masterclass 8–9**. No son una medición automática del catálogo entero.

Separar la dificultad musical del arreglo de la **dificultad dinámica**: el juego puede mostrar menos notas. Para comparar intentos hay que guardar instrumento, arreglo y condiciones. Un 95 % con notas simplificadas no demuestra dominar el arreglo completo.

## Crear o modificar CDLC

Audio que podamos utilizar → tempo → arreglo en EOF → revisión musical → secciones, tonos y DD → DLC Builder/Wwise compatible → prueba dentro del juego. No hace falta construir este flujo para tocar las canciones existentes. No reutilizar el antiguo requisito de Wwise 2013 como regla universal de DLC Builder actual.
