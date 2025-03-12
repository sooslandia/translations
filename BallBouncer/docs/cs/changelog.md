% Historie změn

## 1.3.3

### Nové funkce

- Spanish translation added. Translators:
[rayo-alcantar](https://github.com/rayo-alcantar),
[ogomez92](https://github.com/ogomez92).

### Změny

- Czech translation updated. Translator
[4sensegaming](https://github.com/4sensegaming).

### Opravy

- Opravena kritická chyba, ke které docházelo, když se ozývalo mnoho zvuků
zároveň.
- Fixed issues with star modules.
   - Additional module information tab now updates when you buy upgrades.
   - The description of the "ball controller" module's controlled ball speed
increase no longer includes the information about the twelve percent speed
increase.
   - When pressing the key to check the current amount of star energy, the number is
now announced at the beginning of the message.
   - Fixed a critical bug when activating the "ball controller" star module and the
ball was caught during activation.
- Fixed the completion tracking of the "Magnetism" skill usage quest in training
mode.
- Recording issues fixed.
   - When closing the game using Alt+F4 during gameplay, the recording is canceled
if the "Cancel recording when manually aborting the game" checkbox is checked
and properly finalized if it is not checked.
   - When the game ends prematurely due to reaching -1000 points, the recording is
no longer canceled even if the "Cancel recording when manually aborting the
game" checkbox is checked.
- It is now possible to play with jaws active.
- Fixed an issue with launching the game on Windows for some users.

## 1.3.2

### Opravy

- Opraven zvuk trefy pálkou do míče, takže se teď přehrává ve všech zamýšlených
situacích.
- Do popisu režimů Zkouška vůle a Mistrovská zkouška byly doplněny informace o
tom, jak aktivovat předměty.
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
- Upraveno vyvážení bonusových bodů získaných za dlouhé série nárazů do předmětů,
zničení předmětů a odrazů míče od stropu.
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
- Opraveno nastavování úrovní schopností v režimu tréninku.
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
   - Srbština. Překladatel [nidza07](https://github.com/nidza07).
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
   - Turečtina. Překladatel [fatihyuksek](https://github.com/fatihyuksek1).
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
- Režim tréninku se také dočkal vylepšení.
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
- Přidány dočasné alternativní klávesy pro horizontální a vertikální máchnutí
pálkou.
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
- Aura vítěze nyní nezvyšuje počet bodů, o které přicházíš kvůli penalizacím.

## 1.0.0

První verze.
