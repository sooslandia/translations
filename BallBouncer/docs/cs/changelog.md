% Historie změn

## 1.4.2

### Změny

- Aktualizované překlady.
   - Turecký. Překladatel [fatihyuksek](https://github.com/fatihyuksek1).
   - Čeština. Překladatel [4sensegaming](https://github.com/4sensegaming).

### Opravy

- Fixed the earlier appearance of the star modules tabs and improvements in the
store.
- Fixed a doubled sound playback when pressing the yes button on the update
screen.

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

### Nové funkce

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

### Změny

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
- Vylepšena schopnost titánský skok. Teď postava doskočí na větší vzdálenost.
- The display of the rewards list shown when opening multiple Luck Chests at once
has been updated.

### Opravy

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

### Změny

- Aktualizované překlady.
   - Srbský. Překladatel [nidza07](https://github.com/nidza07).
   - Turecký. Překladatel [fatihyuksek](https://github.com/fatihyuksek1).
- Upravena kritéria pro splnění některých výzev.
- Pokud je aktivní režim sledování míče, nezískáš nyní postih za příliš dlouhé
stání na místě.

### Opravy

- Opravena chyba, kdy bylo možné používat některé aury, když byly zrovna
neaktivní.
- Aura onoho světa byla upravena tak, aby se při jejím použití snadněji
strefovalo do míče.
- Opraveno chování elektrického výboje v režimu Zkouška rychlosti, kdy mohl
zasáhnout postavu a zároveň být započítán tak, že se mu hráč vyhnul.
- Opravena kritická chyba při současném použití schopností "magnetismus" a
"raketový útok".
- Opravena kritická chyba při současném použití schopností "duch chytače" a
"titánský skok".
- Pravděpodobně opravena kritická chyba, ke které docházelo během restartování
hry po aktualizaci.
- Opraveno přehrávání zvukových upozornění pro nárazů míče do předmětů v řadě.

## 1.3.4

### Změny

- Aktualizován český překlad. Překladatel
[4sensegaming](https://github.com/4sensegaming).
- Aktualizován španělský překlad. Překladatel:
[ogomez92](https://github.com/ogomez92).
- Pokud není možné aktivovat auru, budeš na to nyní jasně upozorněn/a.
- Pokud nemáš dost energie na aktivaci hvězdného modulu, budeš na to nyní jasně
upozorněn/a.

### Opravy

- Opraven problém s zdsr.
- Chování branky v režimu Zkouška rychlosti bylo opraveno.
   - Branka se teď spustí zpátky do svojí původní výšky po vypršení efektu výtahu.
   - Branka už nemizí z mapy předmětů, když stoupá nebo klesá.
- Opraveno sledování postupu při plnění určitých výzev v režimu Trénink.

## 1.3.3

### Nové funkce

- Přidán španělský překlad. Překladatelé:
[rayo-alcantar](https://github.com/rayo-alcantar),
[ogomez92](https://github.com/ogomez92).

### Změny

- Aktualizován český překlad. Překladatel
[4sensegaming](https://github.com/4sensegaming).

### Opravy

- Opravena kritická chyba, ke které docházelo, když se ozývalo mnoho zvuků
zároveň.
- Opraveny problémy s hvězdnými moduly.
   - Karta "Další informace o modulu" se teď aktualizuje při nákupu vylepšení.
   - U modulu "ovládání míče" už v popisu vylepšení rychlosti ovládaného míče není
informace o dvanáctiprocentním navýšení rychlosti.
   - Při stisku klávesy pro zjištění aktuálního množství hvězdné energie je teď
číslo oznámeno na začátku promluvy.
   - Opravena kritická chybapři aktivaci hvězdného modulu ovládání míče, pokud byl
během aktivace zároveň míč chycen.
- Opraveno sledování postupu při plnění výzvy k používání schopnosti magnetismus
v režimu Trénink.
- Opraveny problémy s nahrávkami.
   - Při zavření hry zkratkou alt+F4 během hry se nahrávka přeruší, pokud je
zaškrtnuto zaškrtávací políčko "Přestat nahrávat při přerušení hry", nebo se
správně uzavře, pokud tato volba zaškrtnuta není.
   - Když hra skončí předčasně, protože skóre kleslo pod minus 1000, nahrávka už se
automaticky neukončí, ani pokud je zaškrtnuto zaškrtávací políčko "Přestat
nahrávat při přerušení hry".
- Nyní je možné hrát se spuštěným JAWSem.
- Opraven problém na některých systémech při spouštění hry na Windows.

## 1.3.2

### Opravy

- Opraven zvuk trefy pálkou do míče, takže se teď přehrává ve všech zamýšlených
situacích.
- Do popisu režimů Zkouška vůle a Mistrovská zkouška byly doplněny informace o
tom, jak aktivovat speciální předměty.
- Opraven pád hry při používání jiného odečítače než NVDA.
- Opraveny problémy s nahrávkami ve formátu MP3.
   - Snad opraven pád hry, ke kterému docházelo při zapnutém nahrávání.
   - K nahrávkám se nyní přidává speciální VBR hlavička. Její absence mohla před
touto verzí způsobovat v některých přehrávačích nesprávné zobrazování délky
nahrávky a problémy při přetáčení.
   - Byly upraveny parametry MP3 enkodéru, aby se snížila velikost souborů bez
znatelné ztráty kvality.
- Do dokumentace byl doplněn řádek, který vysvětluje, jak je možné odemknout
cestu výzev (v části Další režimy hry).
- Opravena kritická chyba, ke které docházelo, když se ozývalo mnoho zvuků
zároveň.

## 1.3.1

Opravena chyba při přehrávání zvuků předmětů ve stereu.

## 1.3.0

Tohle je zatím největší aktualizace, která do hry přidává obrovské množství
nového obsahu.

Čekají na tebe tři nové režimy hry, z nichž každý se dá vylepšovat, spolu s
cestou výzev, na které narazíš na desítky rozmanitých úkolů. Plněním těchto
výzev můžeš získávat hvězdy, které se poté dají utrácet za nejrůznější vylepšení.

Nové předměty ti pomůžou dosahovat mnohem větších skóre, než by se ti kdy zdálo
možné.

Nové aury vdechnou nový život tvým schopnostem, zatímco nové schopnosti ti
otevřou ještě více strategií, jak efektivně ničit předměty.

A pak jsou tu samozřejmě ještě další vylepšení ovlivňující celkovou hratelnost,
která ti umožní vyhnat skóre až do nepředstavitelných výšin a rozpoutat na hrací
ploše ještě zběsilejší destrukci.

Pokud chceš dosáhnout skutečného vrcholu, budeš muset ve hře strávit desítky
hodin, ale ničeho se neboj — tento čas bude vrchovatě naplněný nespoutaným
chaosem ničení a sladkou chutí bohatě zasloužených odměn!

### Nové funkce

- Přidán nový obsah.
   - Tři nové režimy hry, každý se svou vlastní měnou.
   - Cesta výzev.
   - Nové statistické milníky.
   - Nové předměty, schopnosti a aury, které se odemykají pomocí měn z nových
herních režimů.
   - Stejně jako spousta různých vylepšení, která mají vliv jak na nové režimy, tak
na normální hru.
- Přidána možnost zobrazit si popis jednotlivých režimů hry.
   - Chceš-li si zobrazit popis některého režimu, vyber ho v seznamu na nové
obrazovce spuštění hry a stiskni klávesu D, případně klikni na tlačítko
"Otevřít popis režimu".

### Změny

- Aury teď můžou být aktivní nebo neaktivní.
   - Na začátku můžeš v jednu chvíli používat pouze dvě aury zároveň, ale časem
získáš možnost počet aktivních aur zvýšit, stejně jako odemknout úplně nové
aury.
   - Nyní si také můžeš zobrazit popisy jednotlivých aur, s výjimkou aury vítěze a
času, stisknutím příslušného tlačítka na kartě Aury v profilu.
- Vylepšena schopnost titánský skok. Teď postava doskočí na větší vzdálenost.
- Upraveno vyvážení bonusových bodů získaných za dlouhé série nárazů míče do
předmětů, zničení předmětů a odrazů míče od stropu.
- Cena za vylepšování aury vítěze a aury času byla zvýšena. Pokud máš některou z
těchto aur aktuálně na vyšší než páté úrovni, vynuluje se a úspěchové body
investované do jejího vylepšování se ti vrátí.
- Položky v nabídkách se teď dají potvrzovat také numerickým enterem a je možné i
enter podržet pro rychlou opakovanou aktivaci stejné položky.
- Výpočet získaných mincí byl upraven pro konečná skóre vyšší než dva miliony.
- Chování přehrávání zvuku při zjišťování pozice postavy se změnilo.
   - Dřív: Zvuk se ozýval z pozice postavy v režimu pohledu ze středu plochy a ze
středu plochy v režimu pohledu z pozice postavy.
   - Nyní: Zvuk se vždycky ozve z pozice postavy, kromě případu, kdy je aktivní
pohled z pozice postavy a zároveň je vypnutý režim sledování míče. Jedině v
tomto případě se zvuk ozve ze středu plochy.
- Obrazovka seznámení se zvuky byla přepracována.
   - Menu nahradil virtuální dialog.
   - Základní zvuky hry i zvuky jednotlivých nových režimů jsou nyní rozděleny do
příslušných karet dialogu, aby se po nich lépe pohybovalo a daly se přehrávat
i přímo během hry.
- Změnil se způsob nahrávání hry.
   - Nahrávky se teď ukládají ve formátu MP3.
   - Starý způsob nahrávání už nefunguje, ale nahrávky ve starém formátu se pořád
přehrávat dají.
   - Nové nahrávky budou umístěny ve složce "userData/mp3recordings".
   - Možnost přehrávat nahrávky ve starém formátu bude odstraněna ve verzi 1.5.0.
- Drobné úpravy a opravy nekonzistencí v anglickém překladu.
- Opraveno nastavování úrovní schopností v režimu Trénink.
   - Nastavené úrovně schopností se teď reálně projeví ve hře.
   - Nyní je také možné nastavit schopnosti na libovolnou úroveň až po dostupné
maximum.
- Opravena kritická chyba při změně nastavení ovládání během hry.
- Opravena chyba, kdy kamera nesledovala postavu při skákání nebo použití
schopnosti titánský skok.
- Zvýšena přesnost trefy postavy do míče při použití schopnosti titánský skok.
- Když postava vyskočí, vynuluje se teď časovač pro postih za příliš dlouhé stání
na místě bez pohybu.
- Opravena chyba, která umožňovala otevření mapy předmětů a zapauzování hry
zároveň, což vedlo ke zvláštnímu a nežádoucímu chování.
- Opravena chyba ve výpočtu bodů získaných za zničení předmětu. V důsledku této
změny za zničení předmětu nyní získáš méně bodů.
- Opraveno nastavování nesprávných prodlev před dobitím schopností při neúspěšném
pokusu o jejich použití.

## 1.2.4

### Opravy

- Aktualizovány a opraveny překlady.

## 1.2.3

### Nové funkce

- Přidány nové překlady.
   - Srbský. Překladatel [nidza07](https://github.com/nidza07).
   - Čeština. Překladatel [4sensegaming](https://github.com/4sensegaming).

### Opravy

- Opravena drobná chyba v tureckém překladu.
- Opraveno nesprávné zobrazování nápovědy přímo ve hře.
- Opravena potenciální kritická chyba při načítání nahrávky.

## 1.2.2

Aktualizován turecký a indonéský překlad.

## 1.2.1

Tato aktualizace opravuje několik kritických chyb pro uživatele Linuxu.

## 1.2.0

Tato verze se zaměřuje na další vylepšování uživatelského zážitku a dolaďování
stávajícího obsahu. Nyní si můžeš nastavit klávesové zkratky podle vlastního
uvážení. Nyní je možné nahrávat své hraní a přehrávat výsledné nahrávky pomocí
vestavěného přehrávače. K dispozici je také mapa předmětů a několik dalších
vylepšení a oprav.

Otevřeli jsme oficiální [překladový repozitář na
Githubu](https://github.com/sooslandia/translations). Pokud chceš hru přeložit a
máš na to schopnosti, rádi tvoji pomoc přijmeme.

### Nové funkce

- Přidány nové překlady.
   - Turecký. Překladatel [fatihyuksek](https://github.com/fatihyuksek1).
   - Indonéština. Překladatel [MuhammadGagah](https://github.com/MuhammadGagah).
- Nyní můžeš měnit výchozí klávesové zkratky.
   - To provedeš kliknutím na tlačítko "Nastavit klávesové zkratky", které najdeš na
kartě "Klávesové zkratky" na obrazovce Nastavení.
   - Příslušný konfigurační soubor se nachází ve složce s uživatelskými daty hry
("userData") a má název "keyConfig.json". Svou konfiguraci můžeš sdílet s
ostatními uživateli. Aby ti konfigurace někoho jiného fungovala, musíš nahradit
svůj konfigurační soubor tím, který dostaneš od něj.
   - Více informací o nastavení klávesových zkratek najdeš v příslušné části
dokumentace.
- Nyní můžeš nahrávat své hraní.
   - Na aktualizované obrazovce pro výběr režimu hry můžeš zaškrtnout políčko, které
určuje, jestli se tvoje hraní má nahrávat. Chování nahrávání lze
nakonfigurovat na kartě Nahrávání na obrazovce Nastavení.
   - Nahrávky můžeš poslouchat v menu Nahrávky, do kterého se dostaneš příslušnou
položkou hlavního menu.
   - Nahrávky se ukládají do složky "recordings", která se nachází ve složce s
uživatelskými daty hry ("userData"), a mají příponu .sgr. Soubor s nahrávkou
lze v případě potřeby přejmenovat a sdílet s ostatními hráči. Aby hra rozpoznala
nahrávku někoho jiného, musí být umístěna v této složce s nahrávkami.
   - Informace o tom, jak přehrávač nahrávek funguje, a o jeho ovládání najdeš v
příslušné části dokumentace.
- Přidána mapa předmětů.
   - Během hraní ji lze otevřít klávesou M.
   - Po mapě se pohybuješ šipkami. Klávesou O můžeš také zjistit, kolik předmětů se
na mapě nachází.
   - Existují dva režimy pohybu kurzoru po mapě, o kterých se dočteš v příslušné
části dokumentace.
   - Všechny klávesové zkratky pro mapu předmětů lze změnit v nastavení klávesových
zkratek.
- Režim Trénink se také dočkal vylepšení.
   - Klávesou F1 nyní můžeš okamžitě vynulovat prodlevu před dobitím u všech
schopností najednou.
   - Po stisku klávesy F2 se otevře obrazovka, kde můžeš měnit úrovně svých
schopností a rychlost obnovování síly úderu. Na této obrazovce se zobrazují
jen ty schopnosti, které už máš. Jejich úroveň můžeš měnit pouze v rozsahu od 1
až po aktuálně odemčené maximum.
- V nastavení na kartě "Chování" bylo přidáno zaškrtávací políčko, které určuje,
jestli aktuálně zvolený způsob pohledu (z pozice postavy nebo ze středu hrací
plochy) zůstane zachován po dohrání hry.
- Nyní je možné odstranit uložený postup hrou a obnovit výchozí nastavení.
   - Můžeš to udělat v nastavení na kartě "Obecné".
   - Pokud jsi do nastavení vstoupil/a z menu Pauza, obnovit nastavení ani vymazat
svůj postup nemůžeš.

### Změny

- Změnila se obrazovka pro výběr režimu hry.
   - obrazovka se nyní vykresluje ve virtuálním dialogu místo v menu. Navigace na ní
je podobná jako na obrazovce Nastavení nebo Profil.
   - Na nové obrazovce si můžeš vybrat, jestli se má hra nahrávat.
- Vylepšeno rozhraní obrazovky Profil.
   - Nyní lze libovolnou položku ze seznamu statistik zkopírovat do schránky
stisknutím kláves ctrl+C.
   - Na záložce Statistiky je nyní uvedeno, kolik máš aktuálně úspěchových bodů.
   - Aury nyní zobrazují i svůj bonus.
- Mírné změny ve vyvážení hry.
   - Za každých sto bodů až do tisíce teď dostaneš jednu minci. Například jsi
získal/a 678 bodů, v takovém případě dostaneš 7 mincí a ne jednu jako dřív.
   - Až se dostaneš na tisíc bodů, zůstává vše při starém, ale těch prvních 10
mincí, které jsi dostal/a předtím, máš pořád. Například jsi získal/a 1234
bodů, v takovém případě dostaneš 11 mincí.
- Zvýšen maximální počet předmětů na hrací ploše.
- Zvuk po stisku klávesy C v režimu pohledu z pozice postavy se nyní přehrává ze
středu hrací plochy.
- Formát názvu souboru s daty kritické chyby byl změněn na (error yyyy_MM_dd
hh-mm-ss.log)

### Opravy

- Nyní se při zobrazení kritické chyby zvuk zcela ztlumí, místo aby hrál ve
smyčce.
- V některých případech se zlepšila stabilita hry.

## 1.1.1

### Opravy

- Opravena kritická chyba, ke které docházelo, když byl aktivní režim pohledu z
pozice postavy a současně režim sledování míče.
- Opraveno několik dalších drobných chyb.

## 1.1.0

Tato verze se zaměřuje na zlepšování uživatelského zážitku: Zvuk při odpálení
míče, režim pohledu z pozice postavy, alternativní klávesy pro máchnutí pálkou
atd.

### Nové funkce

- Hra nyní podporuje překlady, ve kterých chybí jeden nebo více řetězců. Pokud
není řetězec nalezen, hra místo něj použije odpovídající anglický lokalizační
řetězec.
- V režimu sledování míče nyní strop přehrává zvuk na pozadí, takže sledování teď
bude efektnější.
- Přidán zvuk, který signalizuje úspěšné odpálení míče. Ve výchozím nastavení je
toto upozornění vypnuté; můžeš si ho zapnout v nastavení na kartě "Chování".
- Implementován režim pohledu z pozice postavy. Chceš-li režim přepnout, stiskni
při hře klávesu V.
- Chyby při aktualizaci se nyní zapisují do souboru, který se nachází ve složce
userData/errorLogs.
- Přidány dočasné alternativní klávesy pro vodorovné a svislé máchnutí pálkou.
   - Pro vodorovné máchnutí teď můžeš použít i klávesu e, pro svislé i klávesu r.
   - Toto řešení je dočasné, jen do doby, než bude implementováno nastavení
vlastních klávesových zkratek.
- Položky v seznamu statistik, u kterých je dostupná odměna, jsou nyní na začátku
seznamu.

### Změny

- Zvýšen počet bodů za dokonalé trefy, odrazy míče od stropu a nárazy míče do
předmětů.
- Dokumentace byla aktualizována s ohledem na nové funkce.

### Opravy

- Zvýšena hlasitost zvuku při dopadu po výskoku.
- Aura vítěze nyní nezvyšuje počet bodů, o které přicházíš kvůli postihům.

## 1.0.0

První verze.
