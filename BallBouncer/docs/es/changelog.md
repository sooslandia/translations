% registro de cambios

## 1.4.1

Fixed a critical error when opening profile.

## 1.4.0

This release addresses numerous existing issues, such as the overly complex trial
of mastery mode, difficulties in identifying and activating items, the lack of
stat tracking for completed quests and opened chests, the inability to determine
when the "Furious leap" skill can be activated, and more.

New upgrades have also been added, and statistics milestone reward balancing has
been carried out.

High load on the audio system was resolved, which led to an increase in the
points scored.

### Nuevas características

- Reward for completed quests can now be increased.
   - To access the new screen, click the "Increase reward for completed quests"
button located on the quest board tab in your profile.
   - The increase is made using coins, green, blue, and red orbs.
   - Each of the listed currencies has its own separate enhancement, but they all
collectively affect a single parameter: the chance to get an additional star.
   - If the chance to get an additional star reaches 100%, you will be guaranteed to
receive one extra star as a reward, and the chance counter will reset.
- The trial of mastery mode has been slightly reworked.
   - Balls can no longer collide with one another.
   - The minimum number of objects on the field has been increased.
   - Ball bounces off the ceiling now start a streak and grant a certain number of
points.
   - Perfect strikes have been added.
      - To perform a perfect strike in trial of mastery mode, strike the ball with the
bat when your hit strength is fully restored.
      - If you miss or land a hit without full power, the streak will be reset.
      - The streak and perfect strikes are recorded in the stats.
   - The bonus from the bounce penalty reduction upgrade has been changed from 2% to
5% per level.
   - The mode’s reference information has been updated to reflect the changes made.
- The main menu music has been updated.
   - You can now safely share video or audio playthroughs of the game without
turning off the music.
   - Huge thanks to [Nikita K](https://t.me/NikitaKOfficial) for his hard work!
- A sound has been added to notify you when a quest is completed.
- A new upgrade has been added that increases the bonus for dodging electric
discharges in trial of speed mode.
- New star upgrades added.
   - Duration of Destruction, Collision, and Ceiling Bounce Streaks increase.
   - Indulgence of Inaction.
- You can now find out how high the ball is.
   - The default key for the function is B.
   - When used, you will hear information about how high the ball is, along with a
special sound played in the ball’s current pitch.
   - In trial of mastery mode, the positions of all balls on the field will be
announced in order, and the sound will be played in the pitch of the ball that
is the lowest.
- New statistics items added.
   - Total luck chests opened.
   - Total quests completed.
- Sound panning customization has been added.
   - To access this screen, press the corresponding button on the settings screen,
on the "Sound" tab.
   - To get help information about the function, press the "Help" button on the
sound panning settings screen.
- You can now disable the generation of mines, couches, and toolboxes on the game
field.
   - A list of checkboxes has been added to the mode selection screen, allowing you
to toggle the generation of specific objects on or off.
   - The list will be hidden if the mode selection cursor is set to any mode other
than Normal or Training.
- A feature has been added that allows you to switch between ready to use skills.
   - Switch to the next ready to use skill: Equals (=) key or Numpad Minus (-).
   - Switch to the previous ready to use skill: Hyphen (-) key or Numpad Multiply
(*).
   - The keys apply to the default controls configuration.
- A new setting has been added that allows you to disable the countdown at the
start of the game.
- A feature has been added that allows you to change the ball's sound on the fly.
   - To change the sound, enter Ball watch mode during a game session, then press
the L key to cycle through sounds.
   - In trial of mastery mode, this feature works similarly. Use the J key to select
the ball whose sound you want to change, then press the L key.
   - By pressing the F1 key during a trial of mastery game session, you'll open the
ball sound customization screen, where you can adjust the sounds in a calm
environment.
      - The screen contains four elements: three lists, each corresponding to a
specific ball, and a button to close the screen.
      - To preview a ball sound, press the Enter or Space key on the selected item in
any of the lists.
      - You can interrupt the playing sound by navigating through the list or screen.
   - The selected sounds are saved between game sessions.
- A new setting has been added that allows you to normalize the pitch of all ball
sounds to approximately the same level.
   - When previewing sounds in the ball sound selection menu, they play in the same
pitch. However, during gameplay, sounds other than the first one still don’t
fully match its pitch.
   - Despite this, the feature can be useful for those who use ball sounds other
than the first and have trouble distinguishing sounds in noisy environments,
as raising the pitch also increases audibility.
- A new setting has been added that allows you to switch to Ball watch mode with
a key press instead of holding the key down.
- The pause menu now includes the option to view the skills assigned to slots
(under "Active Skills").

### Cambios

- Now, in trial of will and Mastery modes, if you are near an item and can
activate it, the item's sound pitch is slightly increased.
- The penalty for the ball bouncing off the floor has been adjusted.
   - if the ball bounces off the floor 40 times in a row, the penalty for subsequent
bounces will increase very rapidly.
   - This change is offset by the new upgrade "Indulgence of Inaction".
- The reward for opening Luck Chests has been increased.
- Some changes have been made to the rewards for reaching stat milestones. If any
discrepancies are detected when the game starts, previously allocated
achievement points will be reset and rewards will be recalculated.
- In trial of will and trial of mastery modes, the same type of item can no
longer appear more than twice in a row.
- In trial of speed mode, the same effect can no longer appear twice in a row.
- Store changes: the Time Aura and Leader Aura upgrades have been moved to the
"Auras" tab; the "Increased Chance of Special Object Spawns" upgrade has been
moved to the "Objects" tab.
- Rewards for low scores in trial modes have been increased.
- The effect of the upgrade that increases the number of red orbs received has
been improved.
- Coin reward calculation has been improved for final scores over 100 million.
- If you’ve purchased the maximum number of quest slots, the purchase button will
now be hidden from the screen.
- La habilidad "Salto furioso" ha sido mejorada. Ahora el personaje puede
lanzarse a una mayor distancia.
- The display of the rewards list shown when opening multiple Luck Chests at once
has been updated.

### Arreglos

- Handling of a large number of simultaneously playing sounds has been improved.
   - As a result of this optimization, the total number of sounds during the
destruction of many objects has been reduced. However, the audio environment
can still become overloaded.
   - You may also notice that you're scoring significantly more points during Normal
mode gameplay. This is expected and happens because a major overload in the
audio system—previously causing overall game slowdown—has been resolved.
- Fixed a rare freeze and crash that could occur right after starting a game
session when gameplay recording was enabled.
- Fixed an issue where receiving a bonus for destroying a puppet or dodging an
electric discharge could increase a negative score.
- Fixed incorrect behavior that occurred when using the "Furious leap" skill.
- The progress for the quest "Hit the ceiling with the ball while the
immateriality effect is active" now also counts when using the "ball
controller" star module.
- Improved the handling of chest and quest reset time updates.
- Descriptions of some upgrades in the store have been expanded.
- You can now skip the coin and other currency gain animation by pressing the
Enter key on the numpad.

## 1.3.5

### Cambios

- Updated translations.
   - Traductor serbio [nidza07](https://github.com/nidza07).
   - Traductor turco [fatihyuksek](https://github.com/fatihyuksek1).
- Changed the completion criteria for some quests.
- Now, if the ball watch mode is enabled, the penalty for the character staying
in one place is not applied.

### Arreglos

- Fixed the ability to use certain auras if they are not active.
- Otherworldly aura has been changed in such a way as to make it easier to hit
the ball with the bat.
- Fixed the behavior of the electric charge in trial of speed mode, where it
could hit the character and be counted as hitting the ground at the same time.
- Fixed a critical error when using the "Magnetism" and "Rocket Salvo" skills
simultaneously.
- Fixed a critical error when using the "Catcher's Soul" and "Furious Leap"
skills simultaneously.
- Likely fixed a critical error occurring when restarting the game after an
update.
- Fixed the sound playback for the object collision streak notification.

## 1.3.4

### Cambios

- Traducción al checo actualizada. Traductor
[4sensegaming](https://github.com/4sensegaming).
- Spanish translation updated. Translator:
[ogomez92](https://github.com/ogomez92).
- If you are unable to activate an aura, you will now be notified clearly.
- If you do not have enough energy to activate a star module, you will now be
notified when attempting to activate it.

### Arreglos

- Fixed an issue with zdsr.
- The behavior of the goal in the trial of speed mode has been fixed.
   - Now the goal lowers back to its original height after the "Elevator" effect
ends.
   - The goal will no longer disappear from the object map when rising or lowering.
- Fixed the completion tracking of certain quests in training mode.

## 1.3.3

### Nuevas características

- Traducción al español añadida. Traductores:
[rayo-alcantar](https://github.com/rayo-alcantar),
[ogomez92](https://github.com/ogomez92).

### Cambios

- Traducción al checo actualizada. Traductor
[4sensegaming](https://github.com/4sensegaming).

### Arreglos

- Se corrigió un error crítico que ocurría cuando se reproducían muchos sonidos
simultáneamente.
- Se solucionaron problemas con los módulos estrella.
   - La pestaña de información adicional del módulo ahora se actualiza cuando
compras mejoras.
   - La descripción del módulo "controlador de bola" ya no incluye la información
sobre el aumento de velocidad del doce por ciento.
   - Al presionar la tecla para comprobar la cantidad actual de energía estelar, el
número ahora se anuncia al principio del mensaje.
   - Se corrigió un error crítico al activar el módulo estelar "controlador de bola"
y la bola era atrapada durante la activación.
- Se ha corregido el seguimiento de la finalización de la misión de uso de la
habilidad "Magnetismo" en el modo de entrenamiento.
- Problemas de grabación solucionados.
   - Al cerrar el juego usando Alt+F4 durante la partida, la grabación se cancela si
la casilla "Cancelar grabación al abortar el juego manualmente" está marcada y
se finaliza correctamente si no lo está.
   - Cuando el juego termina prematuramente al alcanzar -1000 puntos, la grabación
ya no se cancela incluso si la casilla "Cancelar grabación al abortar el juego
manualmente" está marcada.
- Ahora es posible jugar con mandíbulas activas.
- Se solucionó un problema al iniciar el juego en Windows para algunos usuarios.

## 1.3.2

### Arreglos

- Se ha corregido el sonido exitoso del bate y ahora se reproduce en todas las
situaciones previstas.
- Se ha añadido información sobre cómo activar objetos en las descripciones de
los modos prueba de voluntad y prueba de maestría.
- Se ha solucionado un fallo del juego que ocurría cuando un lector de pantalla
distinto de NVDA estaba activo.
- Se han solucionado los problemas con las grabaciones mp3.
   - Posiblemente se haya solucionado un fallo del juego que ocurría al jugar con la
grabación activada.
   - Ahora se añade un encabezado VBR especial a las grabaciones. Anteriormente, su
ausencia podía hacer que algunos reproductores mostraran incorrectamente la
duración de la grabación y tuvieran problemas al buscar.
   - Se han ajustado los parámetros de codificación MP3 para reducir el tamaño del
archivo sin pérdida de calidad notable.
- Se ha añadido una línea a la documentación explicando cómo desbloquear el
tablón de misiones (en la sección "Otros modos de juego").
- Se corrigió un error crítico que ocurría cuando se reproducían muchos sonidos
simultáneamente.

## 1.3.1

Se corrigió un error con el paneo de sonido de los objetos.

## 1.3.0

Esta es la actualización más grande, añadiendo mucho contenido nuevo al juego.

Te esperan tres modos nuevos, cada uno de los cuales se puede mejorar, junto con
el contenido del tablón de misiones que presenta docenas de misiones diversas.
Al completar estas misiones, puedes ganar estrellas, que luego se pueden gastar
en varias mejoras.

Los nuevos objetos te ayudarán a conseguir más puntos de los que jamás habrías
imaginado.

Las nuevas auras darán nueva vida a tus habilidades, mientras que las nuevas
habilidades abrirán aún más estrategias para la destrucción de objetos.

Y, por supuesto, están las mejoras que afectan a toda la jugabilidad,
permitiéndote acumular puntos a niveles sin precedentes y crear aún más
destrucción en el campo de juego.

Para alcanzar las verdaderas alturas, tendrás que pasar docenas de horas, pero no
te asustes: esas horas estarán llenas de un caos desenfrenado de destrucción y
la dulzura de recompensas bien merecidas.

### Nuevas características

- Nuevo contenido añadido.
   - Tres modos nuevos, cada uno con su propia moneda.
   - Un tablón de misiones.
   - Nuevos elementos de estadísticas.
   - Nuevos objetos, habilidades y auras, desbloqueados con las monedas de los
nuevos modos.
   - Así como muchas mejoras diferentes que afectan tanto a los nuevos modos como al
juego normal.
- Se ha añadido la capacidad de ver las descripciones de los modos de juego.
   - Para abrir la descripción, selecciona un modo de la lista en la pantalla de
inicio de un nuevo juego y pulsa la tecla D, o haz clic en el botón "Abrir
descripción del modo".

### Cambios

- Ahora las auras pueden estar activas o inactivas.
   - Inicialmente, puedes usar solo dos auras al mismo tiempo, pero en el futuro, se
puede aumentar el número de auras activas, así como adquirir nuevas.
   - También puedes abrir la descripción de un aura, excepto las auras de líder y de
tiempo, pulsando el botón correspondiente en la pestaña de auras del perfil.
- La habilidad "Salto furioso" ha sido mejorada. Ahora el personaje puede
lanzarse a una mayor distancia.
- Se ha ajustado el equilibrio de puntos otorgados por altas rachas de
colisiones, destrucción de objetos y rebotes de la pelota en el techo.
- El coste de mejora para las auras de Líder y Tiempo ha aumentado. Si tu nivel
de aura es superior a cinco, se restablecerá a cero y se te devolverán los
puntos de logro gastados en mejorarlo.
- Ahora puedes activar elementos del menú presionando la tecla Enter del teclado
numérico, y también mantener Enter en los botones para activaciones rápidas.
- El cálculo de la recompensa de monedas se ha refinado para las puntuaciones
finales superiores a dos millones.
- Se ha cambiado el comportamiento de la reproducción de sonido para comprobar la
posición del personaje.
   - Anteriormente: El sonido se reproducía en la posición del personaje en la vista
del centro del campo, y se reproducía en el centro del campo en la vista en
primera persona.
   - Ahora: El sonido siempre se reproduce en la posición del personaje, excepto
cuando la vista en primera persona está activa y el modo de seguimiento de la
pelota está desactivado. En este caso, el sonido se reproduce en el centro del
campo.
- La pantalla de aprender sonidos ha sido rediseñada.
   - El menú ha sido reemplazado por un formulario virtual.
   - Los sonidos, tanto del juego base como de los nuevos modos, ahora están
organizados en pestañas separadas del formulario para facilitar la navegación
y la posibilidad de escucharlos durante el juego.
- El método de grabación de la partida ha cambiado.
   - Ahora, las grabaciones se guardan en formato MP3.
   - El método de grabación antiguo ha sido desactivado, pero aún es posible
reproducir archivos grabados anteriormente.
   - Las nuevas grabaciones estarán ubicadas en userData/mp3recordings.
   - La capacidad de reproducir grabaciones en el formato antiguo se eliminará en la
versión 1.5.0.
- Se corrigieron pequeños cambios e inconsistencias en la traducción al español.
- Se ha solucionado el ajuste de niveles de habilidad en el modo de entrenamiento.
   - Ahora, cambiar los niveles de habilidad tendrá un efecto en la sesión de juego.
   - Además, ahora puedes establecer cualquier nivel de habilidad hasta el máximo
posible.
- Se ha corregido un error crítico al cambiar la configuración de controles
durante el juego.
- Se ha solucionado el problema por el cual la cámara no seguía al personaje
durante un salto o al usar la habilidad "Salto furioso".
- Se ha aumentado la precisión del golpe del personaje en la pelota al usar la
habilidad "Salto furioso".
- Ahora, cuando el personaje salta, el temporizador de penalización por quedarse
en un lugar se reinicia.
- Se ha solucionado el problema que permitía abrir el mapa de objetos y pausar el
juego al mismo tiempo, lo que provocaba un comportamiento extraño e indeseado.
- Se ha corregido el error en el cálculo de puntos por la destrucción de objetos.
Como resultado, ahora se otorgan menos puntos por esto.
- Se ha corregido la configuración incorrecta del tiempo de reutilización de la
habilidad tras un intento fallido.

## 1.2.4

### Arreglos

- Traducciones actualizadas y corregidas.

## 1.2.3

### Nuevas características

- Nuevas traducciones añadidas.
   - Traductor serbio [nidza07](https://github.com/nidza07).
   - Traductor checo [4sensegaming](https://github.com/4sensegaming).

### Arreglos

- Resuelto un problema menor en la traducción al turco.
- Se corrigió la visualización incorrecta de la ayuda en el juego.
- Se ha corregido un posible error crítico al cargar una grabación.

## 1.2.2

Traducciones actualizadas al turco e indonesio.

## 1.2.1

Esta actualización corrige varios errores críticos para usuarios de Linux.

## 1.2.0

Esta versión está destinada a mejorar aún más la experiencia del usuario y pulir
el contenido existente. Ahora puedes reasignar los atajos de teclado como
desees. Ahora es posible grabar tu partida y reproducir las grabaciones
resultantes usando el reproductor integrado para dichas grabaciones. También se
ha incluido un mapa de objetos y varias otras mejoras y correcciones.

Hemos abierto el [repositorio oficial de traducción en
GitHub](https://github.com/sooslandia/translations). Si quieres traducir el
juego y tienes la habilidad, estaremos encantados de aceptar tu ayuda.

### Nuevas características

- Nuevas traducciones añadidas.
   - Traductor turco [fatihyuksek](https://github.com/fatihyuksek1).
   - Traductor indonesio [MuhammadGagah](https://github.com/MuhammadGagah).
- Ahora puedes cambiar los atajos de teclado predeterminados.
   - Para hacer eso, haz clic en el botón "Personalizar atajos de teclado" ubicado
en la pestaña "Configuración de atajos de teclado" en la pantalla de
Configuración.
   - Tu archivo de configuración se encuentra en la carpeta de datos del usuario
(userData) y se llama keyConfig.json. Puedes compartir tu configuración con
otras personas. Para que la configuración de otra persona funcione para ti,
necesitas reemplazar tu archivo de configuración con el que recibiste de esa
persona.
   - Puedes obtener más información sobre la configuración en la sección
correspondiente de la documentación.
- Ahora puedes grabar tu partida.
   - Puedes marcar la casilla que determina si tu sesión de juego se grabará en la
pantalla actualizada de selección de modo de juego. El comportamiento de la
grabación se puede configurar en la pestaña de Grabación de la pantalla de
Configuración.
   - Puedes reproducir grabaciones desde el menú de grabaciones, al que puedes
acceder activando el elemento correspondiente en el menú principal.
   - Las grabaciones se guardan en la carpeta de grabaciones, ubicada en la carpeta
de datos del usuario (userData) y tienen una extensión .sgr. El archivo de
grabación se puede renombrar si es necesario y compartir con otras personas.
Para que la grabación de otra persona sea detectada por el juego, debe colocarse
en la carpeta de grabaciones del juego.
   - La información sobre cómo funciona el reproductor de grabación y sus teclas de
control se puede encontrar en la sección correspondiente de la documentación.
- Mapa de objetos añadido.
   - Se puede abrir con la tecla m durante una partida.
   - Navega por el mapa usando las teclas de flecha. También puedes averiguar
cuántos objetos hay en el mapa pulsando la tecla o.
   - Hay dos modos de navegación, sobre los cuales puedes leer en la sección
correspondiente de la documentación.
   - Todas las teclas rápidas del mapa de objetos se pueden cambiar en la
configuración de atajos del teclado.
- El modo de entrenamiento también se amplía.
   - Ahora puedes reiniciar al instante el tiempo de reutilización de todas las
habilidades pulsando F1.
   - Cuando presionas la tecla f2, se abrirá una pantalla donde puedes cambiar los
niveles de tus habilidades y la tasa de recuperación de fuerza de golpe. Esta
pantalla solo muestra las habilidades que tienes. Puedes cambiar su nivel solo
en el rango del nivel 1 al nivel máximo actual.
- En la configuración, en la pestaña "Comportamiento", se ha añadido una casilla
que determina si el estado de vista en primera persona se guardará entre
sesiones de juego.
- Ahora es posible borrar el progreso guardado del juego y restablecer la
configuración a los valores predeterminados.
   - Esto se puede hacer en la configuración, en la pestaña "General".
   - No podrás restablecer la configuración ni eliminar tu progreso si accediste a
la configuración a través del menú de pausa.

### Cambios

- La pantalla de selección de modo de juego ha sido modificada.
   - La pantalla ahora se representa mediante un formulario virtual en lugar de un
menú. La navegación es similar a la de la pantalla de configuración o perfil.
   - Desde la nueva pantalla puedes determinar si la sesión de juego se grabará.
- Interfaz de pantalla de perfil mejorada.
   - Ahora cualquier elemento de la lista de estadísticas se puede copiar al
portapapeles presionando ctrl+c.
   - La pestaña de estadísticas ahora muestra el número actual de puntos de logros.
   - Las auras ahora muestran también su bonificación.
- Pequeños cambios en el equilibrio del juego.
   - Ahora, por cada cien puntos hasta mil, se otorgará una moneda. Por ejemplo, si
obtuviste 678 puntos, recibirás 7 monedas, y no una como antes.
   - Después de mil puntos, todo sigue igual, pero las 10 monedas recibidas se
quedan contigo. Por ejemplo, si consigues 1234 puntos, recibirás 11 monedas.
- Se ha aumentado el número máximo de objetos en el campo.
- Ahora el sonido que se reproduce al presionar la tecla c en el modo de cámara
en primera persona se reproducirá en el centro del campo.
- El formato del nombre de archivo con datos de error crítico se ha cambiado a
(error yyyy_MM_dd hh-mm-ss.log)

### Arreglos

- Ahora, cuando se muestren errores críticos, el sonido se silenciará por
completo en lugar de repetirse.
- Mejorada la estabilidad del juego en algunos casos.

## 1.1.1

### Arreglos

- Se corrigió un error crítico que ocurría cuando el modo en primera persona y el
modo de seguimiento de la pelota estaban activos al mismo tiempo.
- Se corrigieron otros errores menores.

## 1.1.0

Esta versión se centra en mejorar la experiencia del usuario: sonido de golpe
exitoso del bate, vista en primera persona, teclas alternativas para el swing
del bate, etc.

### Nuevas características

- El juego ahora admite traducciones que faltan en una o más cadenas. Si no se
encuentra una cadena, el juego utiliza las cadenas de localización en inglés.
- En el modo de observación de la pelota, se ha añadido un sonido de fondo al
techo, lo que hará que ver sea más espectacular.
- Se añadió un sonido para indicar cuando el bate golpea la pelota con éxito. Por
defecto, la notificación está desactivada; se activa en la configuración, en
la pestaña "Comportamiento".
- Se ha implementado el modo de cámara en primera persona. Para cambiar entre
modos, pulsa v mientras juegas.
- Los errores durante la actualización ahora se escribirán en un archivo que se
ubicará en la carpeta userData/errorLogs.
- Se añadieron teclas alternativas temporales para realizar golpes horizontales y
verticales con el bate.
   - Para un golpe horizontal, usa la tecla e, para un golpe vertical, usa la tecla
r.
   - Esta solución es temporal y se mantendrá hasta que se implemente la
configuración clave.
- Ahora los objetos con una recompensa disponible en la lista de estadísticas
están al principio de la lista.

### Cambios

- Puntos aumentados por rachas de golpes perfectos, rebotes de la bola en el
techo y rachas de colisiones de la bola con objetos.
- La documentación se ha actualizado para tener en cuenta las nuevas funciones.

### Arreglos

- Se aumentó el volumen del sonido al aterrizar después de un salto.
- Ahora el aura del líder no aumenta los puntos perdidos debido a las
penalizaciones.

## 1.0.0

Lanzamiento inicial.
