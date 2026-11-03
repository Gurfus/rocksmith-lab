# Rocksmith 2014 + UM2 en Linux

Guía de preparación, aún sin validar en el equipo del usuario. Referencias técnicas en [SOURCES.md](../SOURCES.md), especialmente RS ASIO, PipeASIO, RSMods y el manual UM2.

## Información inicial

Anotar distribución, versión, arquitectura, servidor de audio (PipeWire/JACK), Steam nativo o Flatpak, Proton elegido y ruta del juego/prefijo. AppID esperado: **221680**. No publicar datos privados del perfil.

## Orden de pruebas

1. Conectar el bajo al **INST 2** de la UM2 y ajustar Gain 2 sin saturar. Usar auriculares por cable conectados a la interfaz.
2. Confirmar en Linux que la UM2 aparece como entrada y salida y que entra señal del instrumento. Frecuencia inicial: **48 kHz**.
3. Preparar el puente ASIO para Wine/Proton. Ruta prioritaria a investigar: **PipeASIO Manager 1.10.0** con un entorno WoW64 compatible con el juego de 32 bits. Su documentación no soporta Steam Flatpak. WineASIO es otra ruta, no una segunda capa obligatoria.
4. Incorporar **RS ASIO 0.7.5**, siguiendo el README y el INI distribuido. Esta versión incluye correcciones para Proton 11; fijar y registrar la versión que funcione.
5. Seleccionar dentro de Rocksmith la entrada de tipo Real Tone Cable para que RS ASIO la sustituya. No exige un cable Real Tone físico. Empezar con una canción base y el afinador.
6. Cuando el audio funcione, hacer copia de configuraciones y habilitar **un solo CDLC**. Verificar que carga, afina y reconoce notas.
7. Añadir RSMods si hay una función que queramos usar y comprobar otra vez la misma canción.

## Canales y latencia

El jack físico INST 2 suele corresponder al índice ASIO **Channel=1**, si el puente mantiene el orden de las entradas. Un grafo PipeWire que remapee canales puede cambiarlo. `[Asio.Input.0]` identifica el primer jugador, no el primer conector físico.

Comenzar con 256 o 512 frames. A 48 kHz, 256 frames son 5,33 ms **por buffer**, no la latencia total de tocar y oír. Reducir el buffer después de eliminar cortes y verificar la ruta completa.

Para la primera prueba con sonido procesado, dejar **Direct Monitor apagado**. El monitor directo permite oír el bajo aunque el juego no reciba señal y puede producir dos sonidos superpuestos.

El archivo [RS_ASIO.UM2.example.ini](../config/RS_ASIO.UM2.example.ini) es un fragmento orientativo: hay que completar el nombre real del driver usando el registro de RS ASIO y partir del INI de su versión.

## Precauciones de compatibilidad concretas

- La lista de interfaces RS ASIO menciona UM2 con drivers históricos de Windows. En Linux no se instala ese driver de Windows: se usa el dispositivo Linux y el puente ASIO.
- No mezclar NoCableLauncher con la ruta RS ASIO. Las instrucciones y DLL para Rocksmith **2011** no son las de **2014**.
- Los reportes de CDLC Enabler bajo Linux varían por versión y Proton. No dar por hecho que la última DLL falla siempre ni imponer una DLL antigua como requisito universal.
- RSMods documenta `xinput1_3`; el habilitador clásico usa `d3dx9_42`; RS ASIO incluye `avrt`. Los overrides de carga deben combinarse según los componentes realmente instalados. No copiar una línea que borre los anteriores.
- Dejar inicialmente las opciones de RSMods desactivadas y activar de una en una. Conservar copia de los archivos sustituidos.

## Resultado mínimo aceptable

Afinador estable, reconocimiento de notas, una canción base y una custom con bajo, sin cortes persistentes. Registrar versiones, driver, canal, buffer y opciones de lanzamiento cuando funcione. Todavía no hay una configuración universal validada en este repositorio.
