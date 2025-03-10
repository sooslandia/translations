% changelog

## 1.3.2

### Correcciones

- El sonido exitoso del golpe de bate ha sido corregido y ahora se reproduce en todas las situaciones previstas.
- Se ha añadido información sobre cómo activar los objetos en las descripciones de los modos prueba de voluntad y prueba de maestría.
- Se corrigió un fallo del juego que ocurría cuando un lector de pantalla distinto a NVDA estaba activo.
- Se han solucionado problemas con las grabaciones mp3.
  - Posiblemente se corrigió un fallo del juego que ocurría al jugar con la grabación habilitada.
  - Ahora se añade un encabezado VBR especial a las grabaciones. Anteriormente, su ausencia podía causar que algunos reproductores mostraran incorrectamente la duración de la grabación y experimentaran problemas para buscar.
  - Se han ajustado los parámetros de codificación MP3 para reducir el tamaño del archivo sin pérdida notable de calidad.
- Se ha añadido una línea a la documentación que explica cómo desbloquear el tablero de misiones (en la sección "Otros modos de juego").
- Se corrigió un error crítico que ocurría cuando se reproducían muchos sonidos simultáneamente.

## 1.3.1

Se corrigió un error con el paneo del sonido de objetos.

## 1.3.0

Esta es la actualización más grande, agregando mucho contenido nuevo al juego.

Tres nuevos modos te esperan, cada uno de los cuales puede ser mejorado, junto con el contenido del tablero de misiones que presenta docenas de misiones diversas. Al completar estas misiones, puedes ganar estrellas, que luego se pueden gastar en diversas mejoras.

Nuevos objetos te ayudarán a obtener aún más puntos de los que podrías haber imaginado.

Nuevas auras darán nueva vida a tus habilidades, mientras que las nuevas habilidades abrirán aún más estrategias para la destrucción de objetos.

Y, por supuesto, están las mejoras que afectan la jugabilidad en general, permitiéndote acumular puntos a niveles sin precedentes y crear aún más destrucción en el campo de juego.

Para alcanzar las verdaderas alturas, tendrás que pasar docenas de horas, pero no te asustes: ¡esas horas estarán llenas de un caos desenfrenado de destrucción y la dulzura de recompensas bien merecidas!

### Nuevas características

- Se agregó nuevo contenido.
  - Tres nuevos modos, cada uno con su propia moneda.
  - Un tablero de misiones.
  - Nuevos elementos de estadísticas.
  - Nuevos objetos, habilidades y auras, desbloqueadas con las monedas de los nuevos modos.
  - Además de muchas mejoras diferentes que afectan tanto a los nuevos modos como al juego normal.
- Se ha añadido la capacidad de ver las descripciones de los modos de juego.
  - Para abrir la descripción, selecciona un modo de la lista en la nueva pantalla de inicio del juego y presiona la tecla D, o haz clic en el botón "Abrir descripción del modo".

### Cambios

- Ahora las auras pueden estar activas o inactivas.
  - Inicialmente, puedes usar solo dos auras al mismo tiempo, pero en el futuro, el número de auras activas puede aumentar, así como adquirir nuevas.
  - También puedes abrir la descripción de un aura, excepto las auras de líder y de tiempo, presionando el botón correspondiente en la pestaña de auras en el perfil.
- La habilidad "Salto furioso" ha sido mejorada. Ahora el personaje puede lanzarse una mayor distancia.
- Se ha ajustado el balance de puntos otorgados por altas rachas de colisiones, destrucción de objetos y rebotes de bola en el techo.
- El costo de mejora para las auras de Líder y Tiempo ha aumentado. Si tu nivel de aura es superior a cinco, se restablecerá a cero y los puntos de logro gastados en mejorarlo serán devueltos.
- Ahora puedes activar elementos del menú presionando la tecla Enter en el teclado numérico, y también mantener presionado Enter en los botones para activaciones rápidas.
- Se ha refinado el cálculo de la recompensa en monedas para calificaciones finales superiores a dos millones.
- El comportamiento de la reproducción de sonido para verificar la posición del personaje ha cambiado.
  - Anteriormente: El sonido se reproducía en la posición del personaje en la vista central del campo, y se reproducía en el centro del campo en la vista en primera persona.
  - Ahora: El sonido siempre se reproduce en la posición del personaje, excepto cuando la vista en primera persona está activa y el modo de observación de la bola está desactivado. En este caso, el sonido se reproduce en el centro del campo.
- Se ha rediseñado la pantalla de aprender sonidos.
  - El menú ha sido reemplazado por una forma virtual.
  - Los sonidos, tanto del juego base como de los nuevos modos, ahora están organizados en pestañas separadas de la forma para facilitar la navegación y la capacidad de escucharlos durante el juego.
- El método de grabación del juego ha cambiado.
  - Ahora, las grabaciones se guardan en formato MP3.
  - El método antiguo de grabación ha sido deshabilitado, pero aún es posible reproducir archivos grabados previamente.
  - Las nuevas grabaciones estarán ubicadas en userData/mp3recordings.
  - La capacidad de reproducir grabaciones en el formato antiguo será eliminada en la versión 1.5.0.
- Pequeños cambios e inconsistencias corregidas en la traducción al inglés.
- La configuración de niveles de habilidad en el modo de entrenamiento ha sido corregida.
  - Ahora, cambiar los niveles de habilidad tendrá un efecto en la sesión de juego.
  - Además, ahora puedes establecer cualquier nivel de habilidad hasta el máximo posible.
- Se ha corregido un error crítico al cambiar la configuración de controles durante el juego.
- Se ha solucionado el problema donde la cámara no seguía al personaje durante un salto o al usar la habilidad "Salto furioso".
- Se ha aumentado la precisión del golpe del personaje en la bola al usar la habilidad "Salto furioso".
- Ahora, cuando el personaje salta, el temporizador de penalización por quedarse en un lugar se restablece.
- Se ha solucionado el problema que permitía abrir el mapa de objetos y pausar el juego simultáneamente, lo que conducía a un comportamiento extraño e indeseable.
- Se ha corregido el error en el cálculo de puntos por destrucción de objetos. Como resultado, ahora se otorgan menos puntos por esto.
- Se ha corregido la configuración incorrecta del tiempo de reutilización de habilidades después de un intento fallido.

## 1.2.4

### Correcciones

- Traducciones actualizadas y corregidas.

## 1.2.3

### Nuevas características

- Se agregaron nuevas traducciones.
  - Serbio. Traductor [nidza07](https://github.com/nidza07).
  - Checo. Traductor [4sensegaming](https://github.com/4sensegaming).

### Correcciones

- Resuelto un problema menor en la traducción al turco.
- Corrección de la visualización incorrecta de la ayuda en el juego.
- Corrección de un error potencialmente crítico al cargar una grabación.

## 1.2.2

Traducciones actualizadas para turco e indonesio.

## 1.2.1

Esta actualización corrige varios errores críticos para los usuarios de Linux.

## 1.2.0

Esta versión está dirigida a mejorar aún más la experiencia del usuario y pulir el contenido existente. Ahora puedes reasignar atajos de teclado como desees. Ahora es posible grabar tu juego y reproducir las grabaciones resultantes utilizando el reproductor incorporado para tales grabaciones. También se incluye un mapa de objetos y varias otras mejoras y correcciones.

Hemos abierto el [repositorio de traducciones oficial en GitHub](https://github.com/sooslandia/translations). Si deseas traducir el juego y tienes la capacidad, estaremos encantados de aceptar tu ayuda.

### Nuevas características

- Se agregaron nuevas traducciones.
  - Turco. Traductor [fatihyuksek](https://github.com/fatihyuksek1).
  - Indonesio. Traductor [MuhammadGagah](https://github.com/MuhammadGagah).
- Ahora puedes cambiar los atajos de teclado predeterminados.
  - Para hacer eso, haz clic en el botón "Personalizar atajos de teclado" ubicado en la pestaña "Configuración de atajos de teclado" en la pantalla de Configuración.
  - Tu archivo de configuración está ubicado en la carpeta de datos del usuario (userData) y se llama keyConfig.json. Puedes compartir tu configuración con otras personas. Para que la configuración de otra persona funcione para ti, necesitas reemplazar tu archivo de configuración con el que recibiste de la otra persona.
  - Puedes conocer más sobre la configuración en la sección correspondiente de la documentación.
- Ahora puedes grabar tu partida.
  - Puedes marcar la casilla que determina si tu sesión de juego se grabará en la pantalla actualizada de selección de modo de juego. El comportamiento de la grabación se puede configurar en la pestaña Grabación de la pantalla de Configuración.
  - Puedes reproducir grabaciones desde el menú de grabaciones, al que se puede acceder activando el elemento correspondiente en el menú principal.
  - Las grabaciones se guardan en la carpeta de grabaciones, ubicada en la carpeta de datos del usuario (userData) y tienen una extensión .sgr. El archivo de grabación puede ser renombrado si es necesario y compartido con otras personas. Para que la grabación de otra persona sea detectada por el juego, debe ser colocada en la carpeta de grabaciones del juego.
  - La información sobre cómo funciona el reproductor de grabaciones y sus teclas de control se puede encontrar en la sección correspondiente de la documentación.
- Mapa de objetos añadido.
  - Se puede abrir con la tecla m durante una sesión de juego.
  - Navega por el mapa usando las teclas de flechas. También puedes descubrir cuántos objetos hay en el mapa presionando la tecla o.
  - Hay dos modos de navegación, sobre los cuales puedes leer en la sección correspondiente de la documentación.
  - Todos los atajos de teclado del mapa de objetos se pueden cambiar en la configuración de atajos de teclado.
- El modo de entrenamiento también se ha ampliado.
  - Ahora puedes reducir instantáneamente el tiempo de reutilización de todas las habilidades presionando f1.
  - Al presionar la tecla f2, se abrirá una pantalla donde puedes cambiar los niveles de tus habilidades y la tasa de recuperación de fuerza de golpe. Esta pantalla solo muestra las habilidades que tienes. Puedes cambiar su nivel solo en el rango del nivel 1 al nivel máximo actual.
- En la configuración, en la pestaña "Comportamiento", se ha añadido una casilla de verificación que determina si el estado de vista en primera persona se guardará entre sesiones de juego.
- Ahora es posible borrar el progreso de juego guardado y restablecer las configuraciones a los valores predeterminados.
  - Esto se puede hacer en la configuración, en la pestaña "General".
  - No podrás restablecer las configuraciones o borrar tu progreso si accediste a la configuración a través del menú de pausa.

### Cambios

- Se ha cambiado la pantalla de selección de modo de juego.
  - Ahora la pantalla está representada por una forma virtual en lugar de un menú. La navegación es similar a la pantalla de configuración o de perfil.
  - Desde la nueva pantalla puedes determinar si la sesión de juego será grabada.
- Interfaz de pantalla de perfil mejorada.
  - Ahora cualquier elemento de la lista de estadísticas puede ser copiado al portapapeles presionando ctrl+c.
  - La pestaña de estadísticas ahora muestra el número actual de puntos de logro.
  - Las auras ahora muestran su bonificación también.
- Pequeños cambios en el equilibrio del juego.
  - Ahora por cada cien puntos hasta mil, se otorgará una moneda. Por ejemplo, si obtuviste 678 puntos, en este caso recibirás 7 monedas, y no una como antes.
  - Después de mil puntos, todo sigue igual, pero las 10 monedas recibidas permanecen contigo. Por ejemplo, si obtuviste 1234 puntos, en este caso recibirás 11 monedas.
- Se ha aumentado el número máximo de objetos en el campo.
- Ahora el sonido reproducido al presionar la tecla c en el modo de cámara en primera persona se reproducirá en el centro del campo.
- Se ha cambiado el formato del nombre de archivo con datos de errores críticos a (error aaaa_MM_dd hh-mm-ss.log)

### Correcciones

- Ahora, cuando se muestran errores críticos, el sonido se silenciará por completo en lugar de reproducirse en bucle.
- Mejorada la estabilidad del juego en algunos casos.

## 1.1.1

### Correcciones

- Se corrigió un error crítico que ocurría cuando el modo en primera persona y el modo de observación de la bola estaban activos al mismo tiempo.
- Se corrigieron algunos otros errores menores.

## 1.1.0

Esta versión está enfocada en mejorar la experiencia del usuario: sonido exitoso del golpe de bate, vista de cámara en primera persona, teclas alternativas para el golpe de bate, etc.

### Nuevas características

- El juego ahora soporta traducciones que carecen de una o más cadenas. Si no se encuentra una cadena, el juego recurre a las cadenas de localización en inglés.
- En el modo de observación de la bola, se ha añadido un sonido de fondo al techo, lo que ayudará a que la observación sea más espectacular.
- Se agregó un sonido para indicar cuando el bate golpea exitosamente la bola. Por defecto, la notificación está desactivada; se habilita en la configuración, en la pestaña "Comportamiento".
- Implementado el modo de cámara en primera persona. Para alternar entre los modos, presiona v mientras juegas.
- Los errores durante la actualización ahora se escriben en un archivo que estará ubicado en la carpeta userData/errorLogs.
- Se añadieron teclas alternativas temporales para realizar golpes horizontales y verticales con el bate.
  - Para un golpe horizontal, usa la tecla e, para un golpe vertical, usa la tecla r.
  - Esta solución es temporal y permanece hasta que se implemente la configuración de teclas.
- Ahora los elementos con una recompensa disponible en la lista de estadísticas están al principio de la lista.

### Cambios

- Aumentados los puntos recibidos por rachas de golpes perfectos, rebotes de bola en el techo y rachas de colisiones de bola con objetos.
- La documentación ha sido actualizada para tener en cuenta las nuevas características.

### Correcciones

- Se ha aumentado el volumen del sonido al aterrizar después de un salto.
- Ahora el aura del líder no aumenta los puntos perdidos debido a penalizaciones.

## 1.0.0

Lanzamiento inicial.
