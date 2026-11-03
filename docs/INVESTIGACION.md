# Rocksmith en Linux con una Behringer U-Phoria UM2
Investigación cerrada el 2 de noviembre de 2026. Orientada a aprender bajo, tocar heavy/power metal y valorar un pequeño proyecto de desarrollo.

**Recomendación:** empezar por Rocksmith 2014 en Steam, comprobar la licencia que ya tienes y hacer funcionar la UM2 antes de instalar canciones custom. Después, incorporar unos pocos CDLC con arreglo de bajo. Rocksmith+ merece una prueba gratuita si interesa su catálogo, pero no lo elegiría como centro de este proyecto de mods.

Esta es una investigación documental: no he instalado ni probado el juego, la UM2 o los mods en tu ordenador. Las instrucciones de audio son una propuesta verificable, no una configuración ensayada con tu equipo. Aún faltan la distribución de Linux, el tipo de instalación de Steam y tu inventario de licencias.

**1. Por qué se sigue vendiendo un juego que perdió licencias**

| Producto | Qué es | Relación con este proyecto |
| --- | --- | --- |
| Rocksmith original, AppID 205190 | El juego anterior a 2014 | No confundir con las guías de 2014: sus modificaciones y requisitos son diferentes. |
| Rocksmith 2014 / Remastered, AppID 221680 | La plataforma con la comunidad de CDLC que nos interesa | La compra antigua puede conservar su catálogo original. |
| Rocksmith 2014 Learn & Play, también AppID 221680 | La reedición comercial de diciembre de 2024 | Mantiene las funciones centrales, con otro contenido musical incluido. |
| Rocksmith+, AppID 2834910 | Servicio de aprendizaje mediante suscripción | Su Workshop no equivale al sistema de archivos CDLC de 2014. |

El 23 de octubre de 2023 Ubisoft retiró el Rocksmith 2014 original de las tiendas digitales. Anunció retiradas posteriores de DLC y confirmó que los compradores podían seguir descargando y utilizando lo adquirido. El calendario afecta a la venta, no significa que todos los usuarios perdiesen las canciones que ya poseían. [1]

El 19 de diciembre de 2024 apareció Learn & Play. Sustituye las canciones licenciadas del contenido base por material propio de Bachsmith, melodías y ejercicios. La ficha actual advierte que los propietarios anteriores conservan el acceso correspondiente a su edición para evitar perder la música original. El nombre visible de la aplicación en Steam no identifica por sí solo todos tus derechos. [2][3]

El parche Remastered de 2016 y los seis temas de bonificación tampoco son exactamente lo mismo: la actualización de funciones se ofreció a propietarios anteriores, mientras que las canciones extra se distribuían también como DLC. No debemos dar por hecho que tu compra incluye todos esos extras. [4]

Además, Ubisoft declaró en julio de 2026 que trabaja para volver a licenciar algunos DLC populares. Por tanto, no conviene resumir la situación como “desapareció todo para siempre”; hay que consultar cada producto disponible. [5]

**2. Cómo identificar qué compraste y qué tienes completo**

El propietario indica que tiene Rocksmith 2014 Remastered y cree haberlo comprado aproximadamente en 2021. La fecha, el paquete concreto y los DLC aún no se han auditado.

Para resolverlo bastan estas comprobaciones:

| Dato | Dónde comprobarlo | Qué demuestra |
| --- | --- | --- |
| Compra realizada directamente en Steam | Detalles de la cuenta → Historial de compras | Producto y fecha de esa transacción. |
| Juego activado mediante clave o regalo | Detalles de la cuenta → Licencias y activaciones de claves | Nombre del paquete y fecha de activación; esta puede diferir de la compra en otra tienda. |
| DLC oficiales poseídos e instalados | Biblioteca → Rocksmith → Propiedades → DLC | Titularidad y estado de instalación de los complementos que Steam muestra. |
| Archivos descargados de la comunidad | Carpeta dlc del juego | Presencia local de CDLC; no acreditan compras de Steam. |
| Contenido realmente disponible | Lista de canciones dentro del juego | Qué ha cargado esa instalación y perfil. |

Steam recomienda el historial de compra/activación para distinguir ediciones, porque la tienda puede mostrar una edición especial aunque solo se posea la base. Su documentación también explica cómo revisar DLC desde Propiedades. [6][7]

La auditoría debería separar: juego base, seis temas de bonificación de Remastered si corresponden, DLC oficiales comprados, contenido importado del primer Rocksmith si se posee la licencia/herramienta necesaria, y CDLC.

No existe una conclusión fiable del tipo “lo compré antes de tal fecha, luego tengo absolutamente todos los DLC”. Tampoco la fecha de activación reciente de una clave antigua identifica por sí sola su paquete. Antes de comprar otra copia, hay que ver el nombre de la licencia.

El archivo appmanifest_221680.acf ayuda a localizar la instalación y su compilación, pero no sustituye al historial de titularidad. Que Steam muestre Learn & Play en el título de la biblioteca tampoco resuelve esa auditoría.

**3. Dónde están las canciones de la comunidad**

El centro principal es CustomsForge y su buscador Ignition. La página pública consultada muestra aproximadamente 71.000 registros CDLC y unos 3.000 creadores. No son 71.000 canciones únicas de bajo: hay versiones, arreglos y contenido de otros instrumentos. El catálogo completo y las descargas requieren una cuenta gratuita. [8]

El funcionamiento básico para 2014 es instalar un habilitador compatible, obtener un archivo de canción y colocarlo en dlc. Bajo Proton se utiliza la edición de Windows del juego y archivos terminados en _p.psarc; la variante _m.psarc es para el juego de Mac. [9]

El tutorial actual anuncia que no hace falta comprar Cherub Rock para el procedimiento moderno. Las guías antiguas que exigen ese DLC corresponden a otro contexto. Si se recurre a una DLL antigua para solventar una incompatibilidad, hay que revisar también los requisitos de esa versión: no extrapolar automáticamente el comportamiento del instalador nuevo al antiguo. [9][10]

CustomsForge exige derechos sobre el material compartido y prohíbe redistribuir canciones y DLC oficiales de Rocksmith, incluidas modificaciones de ese contenido. No es un sustituto para descargar el catálogo oficial retirado. Para publicar nuestros propios ejercicios, utilizaremos audio propio o con permisos. [11]

**Canciones afines a tus gustos con indicación pública de bajo**

El taller del creador Teinashu identifica arreglos de Gloryhammer como Hootsforce, Universe on Fire y Gloryhammer, y de Alestorm como Drink y Mexico, con marcadores de bajo, repetición de secciones y dificultad dinámica. Es una evidencia del trabajo publicado por el creador, no una comprobación de cada descarga actual. [12]

También encontré participación de una canción de Alestorm en el campeonato de la comunidad, incluyendo la categoría de bajo. Eso confirma que el uso del instrumento no se limita a guitarras. [13]

Antes de añadir cada tema comprobaría:

- Que la entrada incluya Bass/B y que sea el arreglo que buscas.
- Afinación del arreglo de bajo, número de cuerdas y nota más grave.
- Comentarios recientes, versión y posibles enlaces de descarga rotos.
- Presencia de dificultad dinámica y secciones útiles para practicar.
- Sincronización y calidad musical: popularidad no equivale a una transcripción exacta.

Para empezar con tu bajo de cuatro cuerdas seleccionaría material en E estándar o afinaciones cercanas. Clasificar un CDLC por su afinación de guitarra no garantiza que el bajo use la misma. La dificultad de la guitarra tampoco equivale a la del bajo.

**4. La UM2: qué conectar y qué verificar**

El plan se basa en tu aclaración: no hay Real Tone Cable. Hay una U-Phoria UM2 y un cable jack normal de instrumento.

La UM2 dispone de entrada de instrumento independiente INST 2, ganancia propia, monitorización directa y salida de auriculares; admite 48 kHz. Su documentación identifica ese conector como la entrada adecuada para el instrumento. [14][15]

Conexión propuesta:

1. Bajo a INST 2 con el jack normal.
2. UM2 al PC por USB.
3. Auriculares con cable a la UM2.
4. Volumen del bajo abierto y ganancia suficiente sin encender el indicador de saturación al tocar fuerte.
5. Direct Monitor desactivado para comprobar primero únicamente el sonido procesado que devuelve el juego.

La posibilidad de oír una señal directa no demuestra que Rocksmith la esté recibiendo: son recorridos distintos. Primero hay que confirmar la captura digital.

RS ASIO incluye la UM2 en su lista de interfaces reportadas. La nota sobre drivers antiguos de Behringer pertenece al camino de Windows; no es una instrucción para instalar un controlador Windows de la UM2 sobre Linux. La detección real por ALSA/PipeWire debe comprobarse en tu sistema. [16]

**5. La ruta propuesta para Linux**

| Capa | Función |
| --- | --- |
| ALSA/PipeWire | Detectar la UM2 y transportar el audio en Linux. |
| PipeASIO o WineASIO | Exponer una interfaz ASIO al programa Windows. |
| RS ASIO | Permitir a Rocksmith 2014 utilizar esos canales. |
| Steam + Proton | Ejecutar el juego Windows. |

Mi primera opción de investigación es PipeWire + PipeASIO + RS ASIO reciente. WineASIO sigue siendo una alternativa documentada para otros entornos. No hay una única receta que deba aplicarse a todas las distribuciones.

**Versiones verificadas durante esta investigación**

| Proyecto | Versión publicada comprobada | Observación |
| --- | --- | --- |
| RS ASIO | 0.7.5, 9 de agosto de 2026 | Corrige un fallo del parcheador con Proton 11. [17] |
| PipeASIO | 1.10.0, 29 de septiembre de 2026 | Su gestor añade instalación en juegos de Steam con Proton. [18] |
| RSMods | 1.2.8.4, 15 de agosto de 2026 | Incluye correcciones para Learn & Play y calibración. [19] |
| DLC Builder | 3.5.0, 24 de julio de 2025 | Publica paquete para Linux. [20] |
| CDLC Enabler | La página anuncia 4.0, agosto de 2025 | Publicitado para Windows y Learn & Play; eso no garantiza cada combinación con Proton. [10] |

RS ASIO 0.7.5 es especialmente relevante: en la incidencia de agosto dos usuarios confirmaron que la corrección permitió utilizar PipeASIO con Proton nuevo. Las recetas que parten de que “Proton 11 nunca funciona” han quedado desactualizadas. Eso no equivale a una prueba con nuestra UM2. [17][21]

PipeASIO Manager puede instalar y comprobar el controlador en el prefijo elegido. Su documentación indica que la compatibilidad de 32 bits es experimental y requiere el entorno WoW64 apropiado; Rocksmith 2014 es de 32 bits. También dice que el gestor no soporta Steam Flatpak. Esta limitación pertenece a esa vía concreta, no demuestra que Rocksmith sea imposible con cualquier otra configuración Flatpak. [18][22]

Empezaría con Steam instalado como paquete nativo de la distribución si aún se puede elegir. Si ya utilizas Flatpak, primero revisaremos esa situación; no hace falta reinstalar el sistema operativo.

Hay una guía reciente de ferabreu que explica la combinación PipeASIO/Proton. **No hay que copiar su parche del Rocksmith original al 2014:** la propia guía distingue el juego de 2011 de 2014 y remite a RS ASIO para este último. Su fork del primer juego mantiene el requisito de Real Tone Cable, por lo que no es nuestra solución sin cable. [23]

**6. Ajustes iniciales y prueba por etapas**

Antes de instalar CDLC o RSMods:

- Confirmar que PipeWire capta el canal de instrumento de la UM2.
- Establecer 48 kHz y empezar con un búfer conservador, por ejemplo 256 o 512 muestras.
- Mantener inicialmente entrada y salida en la UM2.
- Registrar el controlador ASIO dentro del prefijo de Rocksmith 2014, AppID 221680.
- Instalar RS ASIO y revisar RS_ASIO-log.txt.
- Hacer funcionar una canción incluida antes de añadir otras variables.

256 muestras a 48 kHz representan 5,33 ms por búfer; **no son una medida de la latencia completa**. Habrá que comprobar estabilidad y respuesta real, no perseguir el número más pequeño.

En RS ASIO, Asio.Input.0 significa el primer jugador. Channel selecciona el canal físico/lógico recibido. Si preservamos el orden estéreo natural de la UM2, INST 2 suele corresponder al índice 1, pero el enrutamiento de PipeWire puede cambiarlo. No se debe copiar Channel=0 a ciegas. El archivo de configuración oficial documenta ambos campos por separado. [24]

Este es únicamente un esquema parcial para ese orden de canales:

~~~ini
[Config]
EnableWasapiOutputs=0
EnableWasapiInputs=0
EnableAsio=1

[Asio]
BufferSizeMode=driver

[Asio.Output]
Driver=PipeASIO
BaseChannel=0

[Asio.Input.0]
Driver=PipeASIO
Channel=1

[Asio.Input.1]
Driver=

[Asio.Input.Mic]
Driver=
~~~

Hay que combinarlo con el resto de valores del archivo distribuido, no sobrescribir indiscriminadamente una configuración existente. El nombre de Driver debe coincidir con el que detecte el registro. Si enrutamos el instrumento al primer canal de PipeASIO, cambiaríamos Channel a 0.

El proyecto RS ASIO indica 48 kHz, ExclusiveMode=1 y Win32UltraLowLatencyMode=1, y pide seleccionar en el juego la entrada de cable en lugar de micrófono. Esto es coherente aunque no tengamos el cable físico: el mod introduce el dispositivo de audio correspondiente. También desaconseja mezclarlo con NoCableLauncher. [16]

La guía de PipeASIO distingue su propio búfer de las preferencias genéricas de PipeWire. Un límite global puede dominar una petición por aplicación; poner una variable de entorno aislada no garantiza haber cambiado el búfer efectivo. La selección exacta dependerá de la versión instalada. [22][23]

La prueba mínima debería incluir afinador y notas al aire E/A/D/G, sonido del juego en ambos canales, ausencia de saturación y una canción completa sin cortes. Solo después mediría y reduciría el búfer.

**7. CDLC y Proton: la parte que conviene probar, no prometer**

En enero de 2026 un moderador de CustomsForge describió fallos con el habilitador nuevo en Linux y recomendó una DLL anterior. En mayo otro usuario informó de éxito con la DLL nueva y Proton 9.0-4 siguiendo otra configuración. Hay diferencias reales entre entornos. [25][26]

Por eso no afirmo ni “la última DLL es siempre incompatible” ni “instala la última y funcionará seguro”. Debemos comprobar el ejecutable, Proton, habilitador y DLL cargada.

Plan:

1. Guardar el juego funcional, sus ajustes y el perfil.
2. Ejecutar el habilitador dentro del prefijo correcto mediante protontricks.
3. Verificar la carga de la DLL de CDLC.
4. Añadir un único archivo _p.psarc.
5. Probar que aparece, afina y empieza a tocar sin quedarse bloqueado.
6. Documentar la combinación que funcione y añadir más temas en lotes pequeños.

El override de carga para el habilitador clásico suele involucrar d3dx9_42. RS ASIO y RSMods usan otros componentes; sus overrides deben combinarse si se instalan juntos. No basta con sustituir las opciones de lanzamiento de Steam por la última línea encontrada en un tutorial.

**8. Mods y herramientas que sí merece la pena conocer**

| Herramienta | Utilidad | Encaje |
| --- | --- | --- |
| RS ASIO | Audio mediante interfaces | Prioridad inicial para la UM2. |
| CDLC Enabler | Cargar canciones de la comunidad | Después del audio. |
| RSMods | Cambios de interfaz y práctica | Opcional, instalar progresivamente. |
| CustomsForge Song Manager 1 | Gestión histórica de biblioteca | Consultar como herramienta heredada. |
| CFSM 2 | Gestor nuevo conectado con Ignition | Alfa actual solo para Windows. |
| EOF | Edición de arreglos y sincronización | Para crear nuestros temas. |
| DLC Builder | Empaquetado y validación | Tiene distribución Linux. |
| RockSniffer | Canción actual y estadísticas en tiempo real | Interesante para un futuro panel; compatibilidad exacta bajo Proton por verificar. |
| rs-manager | Biblioteca, estadísticas y listas | Revisar antes de duplicar un gestor. |

RSMods ofrece bucles, rebobinado, cambios de volumen, colores, recarga de biblioteca y otras mejoras. Su README incluye instrucciones para Wine/Proton y el override xinput1_3. No empezaría habilitando todas sus opciones: alguna modifica archivos del juego y otras dependen de la compilación. [27]

CFSM 2 está en alfa 0.2.3. Su página dice que macOS/Linux llegarán después de 1.0; varias funciones todavía no están disponibles. No lo presentaría como aplicación Linux lista ni recomendaría una reparación masiva de la biblioteca recién creada. [28]

RockSniffer muestra información de la canción y algunos datos de juego. Eso demuestra que existe una base técnica para paneles, no que tengamos ya todos los errores nota a nota o una integración Linux terminada. [29]

**9. Crear CDLC propios y reutilizar trabajo existente**

El flujo razonable es elegir audio autorizado, preparar el mapa de tempo, crear o importar el arreglo, revisar notas y técnicas, configurar secciones/tonos, empaquetar y probar dentro del juego.

EOF proporciona el editor. DLC Builder agrupa los componentes y Rocksmith2014.NET incluye bibliotecas de PSARC, SNG, XML, audio y dificultad dinámica. Conviene reutilizar estos formatos y validadores. [20][30][31]

La versión actual del README de DLC Builder admite varias generaciones de Wwise y explica que en Linux utiliza Wine para ejecutar su conversor. El antiguo consejo de “solo sirve Wwise 2013” no se aplica a todos los flujos actuales. La página comunitaria diferencia un paquete histórico para Toolkit de otro para DLC Builder. Hay que seguir los requisitos de la versión elegida. [32][33]

Para TypeScript/Node existe psarcjs, que permite leer arreglos y metadatos. Sería una base para una prueba local; su README menciona una generación antigua de Node, por lo que revisaría dependencias y compatibilidad antes de convertirlo en pieza central de un producto. [34]

rs-manager ya cubre listas, estadísticas y biblioteca. rsrtools ofrece manejo de perfiles y listas, pero su documentación no declara Linux como plataforma soportada. Son referencias útiles; no promesas de integración inmediata. [35][36]

**10. Proyecto prioritario: una carrera con nuestras canciones favoritas**

La idea elegida es un acompañante de Rocksmith con progresión tipo Guitar Hero: capítulos, canciones por dificultad, estrellas y desbloqueos usando CDLC locales de nuestros grupos favoritos. “Nuestras canciones” no exige componer música ni crear todos los arreglos desde cero.

Score Attack y los campeonatos de CustomsForge ya ofrecen puntuación y niveles humanos por instrumento. rs-manager cubre biblioteca, listas y progreso. No he identificado un modo carrera terminado que reúna exactamente esta propuesta y funcione en Linux con nuestros CDLC. Eso es una conclusión limitada de la búsqueda, no una prueba de que no exista ninguno.

El primer prototipo debe comprobar si podemos obtener, bajo Proton, el arreglo tocado y un resultado de intento finalizado mediante RockSniffer u otra integración de lectura. Después podemos construir una campaña pequeña. La especificación, los precedentes y los criterios de éxito están en [MODO_CARRERA.md](MODO_CARRERA.md).

No empezaríamos por modificar el ejecutable, escribir perfiles de Steam ni desarrollar un transcriptor automático de MP3. Un diagnóstico de audio o un generador de ejercicios podrían ser proyectos posteriores, si aparecen necesidades concretas al tocar.

**11. Orden de trabajo que seguiría**

1. Identificar tu licencia y DLC.
2. Anotar distro, versión y si Steam es nativo o Flatpak.
3. Conseguir audio y afinación con UM2.
4. Cargar una canción custom de bajo.
5. Seleccionar una biblioteca inicial pequeña de canciones que te apetezca tocar.
6. Añadir una o dos funciones útiles de RSMods.
7. Elegir un problema observado tras varias sesiones para nuestro primer prototipo.

Criterio de éxito: poder abrir el juego, afinar y tocar una canción sin una sesión de configuración previa. El proyecto de desarrollo debería reducir esa fricción o ayudarte a practicar.

**12. Rocksmith+: críticas y valoración para tu caso**

Las fichas de Steam consultadas rondan el 18 % de reseñas positivas. Las cifras cambian según idioma y captura; es una recepción claramente negativa, no una prueba individual de que a nadie pueda servirle. El producto ofrece una selección gratuita limitada y reserva el catálogo amplio a la suscripción; requiere conexión permanente. [37]

La disponibilidad de contenido puede variar por región y cambiar con las licencias. Workshop permite arreglos dentro de esa plataforma, con las restricciones del catálogo; no debe confundirse con importar cualquier PSARC de 2014. [38][39]

También sería inexacto repetir críticas antiguas como si el catálogo no hubiera mejorado. Ubisoft anunció en 2026 material de artistas relevantes para ti y ya había publicado arreglos oficiales de bajo de Metallica, con arreglos que pueden interesar para practicar. Hay que comprobar su disponibilidad concreta en España antes de pagar. [5][40]

En Linux su documentación oficial sigue pidiendo Windows para PC. La UM2 tampoco figura entre las interfaces concretas certificadas en la lista consultada, aunque la ausencia de esa lista no demuestra incompatibilidad. No he verificado una combinación Rocksmith+ + UM2 + Linux que permita recomendar pagar una suscripción para empezar. [41][42]

Mi elección sigue siendo 2014 para comunidad y desarrollo local. Probaría la parte gratuita de + más adelante si interesa una canción/arreglo oficial concreto; no contrataría un plan largo para resolver nuestra necesidad de CDLC.

**Fuentes**

[1] Ubisoft, retirada de 2014 y calendario de DLC: https://www.ubisoft.com/en-us/game/rocksmith/plus/news-updates/2aWHQHdEaMlORjQqmJwzmg/rocksmith-2014-leaving-stores
[2] Steam, producto 221680 y descripción de Learn & Play: https://store.steampowered.com/app/221680/
[3] Ubisoft en Steam, anuncio del 19/12/2024: https://store.steampowered.com/oldnews/?appgroupname=Rocksmith+2014&appids=221680&enddate=1735718400&feed=steam_community_announcements
[4] Ubisoft, FAQ oficial de Remastered en Steam: https://steamcommunity.com/app/221680/discussions/0/360671352685732676/
[5] Ubisoft, actualización del equipo de julio de 2026: https://www.ubisoft.com/en-us/news/ignt.61846/rocksmith-dev-team-update-where-we-are-what-s-next-and-where-we-stand
[6] Steam, compra y comprobación de edición: https://help.steampowered.com/en/faqs/view/4C10-B32A-137D-0945
[7] Steam, DLC poseídos e instalados: https://help.steampowered.com/en/faqs/view/6948-51E6-E624-8A84
[8] Ignition, catálogo público y funcionamiento: https://ignition4.customsforge.com/
[9] CustomsForge, tutorial de uso de CDLC: https://customsforge.com/topic/901-how-to-use-custom-dlcs-in-rs2014-remastered-updated-for-2023/
[10] CustomsForge, CDLC Enabler: https://ignition4.customsforge.com/tools/cdlcenabler
[11] CustomsForge, normas: https://customsforge.com/guidelines/
[12] Teinashu, taller de arreglos: https://customsforge.com/topic/2937-teinashus-hall-of-glory/
[13] CustomsForge, campeonato con categoría de bajo: https://customsforge.com/topic/64239-rocksmith-2014-championship-week-363/
[14] Behringer, UM2: https://behringer.com/en/products/0805-AAL
[15] Music Tribe, manual de inicio: https://mediadl.musictribe.com/media/sys_master/h1f/h9b/8849476255774.pdf
[16] RS ASIO, README: https://github.com/mdias/rs_asio
[17] RS ASIO 0.7.5: https://github.com/mdias/rs_asio/releases/tag/v0.7.5
[18] PipeASIO 1.10.0: https://github.com/M0n7y5/pipeasio/releases/tag/v1.10.0
[19] RSMods 1.2.8.4: https://github.com/Lovrom8/RSMods/releases/tag/RSModsInstaller-v1.2.8.4_OnCommit
[20] DLC Builder, distribución y descarga Linux: https://ignition4.customsforge.com/tools/dlc-builder
[21] RS ASIO, incidencia 629 y confirmaciones: https://github.com/mdias/rs_asio/issues/629
[22] PipeASIO, README y gestor: https://github.com/M0n7y5/pipeasio
[23] Ferabreu, guía que distingue 2011/2014: https://github.com/ferabreu/rocksmith-on-linux/blob/main/docs/setup-guide.md
[24] RS ASIO, configuración distribuida: https://github.com/mdias/rs_asio/blob/master/dist/RS_ASIO.ini
[25] CustomsForge, reportes de incompatibilidad Linux: https://customsforge.com/topic/901-how-to-use-custom-dlcs-in-rs2014-remastered-updated-for-2023/page/61/
[26] CustomsForge, reporte de éxito con otro entorno: https://customsforge.com/topic/901-how-to-use-custom-dlcs-in-rs2014-remastered-updated-for-2023/page/62/
[27] RSMods, funciones e instrucciones Wine/Proton: https://github.com/Lovrom8/RSMods
[28] CFSM 2, estado de alfa y plataformas: https://ignition4.customsforge.com/tools/cfsm2
[29] RockSniffer: https://github.com/kokolihapihvi/RockSniffer
[30] EOF: https://editoronfire.com/
[31] Rocksmith2014.NET: https://github.com/iminashi/Rocksmith2014.NET
[32] DLC Builder, README técnico: https://github.com/iminashi/Rocksmith2014.NET/blob/main/samples/DLCBuilder/README.md
[33] CustomsForge, versiones Wwise por flujo: https://ignition4.customsforge.com/tools/wwise
[34] psarcjs: https://github.com/sandiz/psarcjs
[35] rs-manager: https://github.com/sandiz/rs-manager
[36] rsrtools: https://github.com/BuongiornoTexas/rsrtools
[37] Rocksmith+ en Steam: https://store.steampowered.com/app/2834910/?l=spanish
[38] Ubisoft, condiciones de la suscripción: https://www.ubisoft.com/legal/documents/RocksmithPlusTerms/en-INTL
[39] Ubisoft, herramientas de música licenciada: https://www.ubisoft.com/en-us/game/rocksmith/plus/news-updates/6IC8IW6PcCDeN5eALffPxy/new-songs-now-available-in-rocksmith
[40] Ubisoft, Metallica y arreglos de bajo: https://www.ubisoft.com/en-us/game/rocksmith/plus/news-updates/6ZlN9DyrTGnEoTYL69xfyz/january-23-2024-song-drop
[41] Ubisoft, requisitos de Rocksmith+: https://store.ubisoft.com/eu/rocksmithplus/660ecb20fbff4e2940488bf4.html?lang=en-SE
[42] Ubisoft, periféricos soportados de Rocksmith+: https://www.ubisoft.com/en-us/help/rocksmith-plus/purchases-and-rewards/article/supported-peripherals-for-rocksmith/000103038
