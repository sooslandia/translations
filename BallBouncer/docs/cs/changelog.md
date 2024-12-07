% Historie změn

## 1.2.4

### Opravy

- Updated and corrected translations.

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

Tato verze se zaměřuje na další vylepšování uživatelského prostředí a dolaďování
stávajícího obsahu. Nyní si můžeš nastavit klávesové zkratky podle vlastního
uvážení. Nyní je možné nahrávat své hraní a přehrávat výsledné nahrávky pomocí
vestavěného přehrávače. K dispozici je také mapa předmětů a několik dalších
vylepšení a oprav.

Otevřeli jsme oficiální překladový repozitář
[github](https://github.com/sooslandia/translations). Pokud chceš hru přeložit a
máš na to schopnosti, rádi tvoji pomoc přijmeme.

### Nové funkce

- Přidány nové překlady.
   - Turečtina. Překladatel [fatihyuksek](https://github.com/fatihyuksek1).
   - Indonéština. Překladatel [MuhammadGagah](https://github.com/MuhammadGagah).
- Nyní můžeš měnit výchozí klávesové zkratky.
   - To provedeš kliknutím na tlačítko "Nastavit klávesové zkratky", které najdeš na
kartě "Nastavení klávesových zkratek" na obrazovce Nastavení.
   - Konfigurační soubor se nachází ve složce userData a jmenuje se keyConfig.json.
Svou konfiguraci můžeš sdílet s ostatními uživateli. Aby ti konfigurace někoho
jiného fungovala, musíš nahradit svůj konfigurační soubor tím, který dostaneš od
něj.
   - Více informací o nastavení klávesových zkratek najdeš v příslušné části
dokumentace.
- Nyní můžeš nahrávat své hraní.
   - Na aktualizované obrazovce pro výběr režimu hry můžeš zaškrtnout políčko, které
určuje, jestli se tvoje hraní má nahrávat. Chování nahrávání lze
nakonfigurovat na kartě Nahrávání na obrazovce Nastavení.
   - Nahrávky můžeš poslouchat v menu Nahrávky, do kterého se dostaneš příslušnou
položkou hlavního menu.
   - Nahrávky se ukládají do složky Recordings, která se nachází ve složce userData,
a mají příponu .sgr. Soubor s nahrávkou lze v případě potřeby přejmenovat a
sdílet s ostatními hráči. Aby hra rozpoznala nahrávku někoho jiného, musí být
umístěna v této složce s nahrávkami.
   - Informace o tom, jak přehrávač nahrávek funguje, a o jeho ovládání najdeš v
příslušné části dokumentace.
- Přidána mapa předmětů.
   - Během hraní ji lze otevřít klávesou M.
   - Po mapě se pohybuješ šipkami. Klávesou O můžeš také zjistit, kolik předmětů se
na mapě nachází.
   - Existují dva režimy pohybu kurzoru, o kterých se dočteš v příslušné části
dokumentace.
   - Všechny klávesové zkratky pro mapu předmětů lze změnit v konfigurátoru
klávesových zkratek.
- Režim Trénink se také dočkal vylepšení.
   - Klávesou F1 nyní můžeš okamžitě vynulovat prodlevu před dalším použitím u všech
schopností najednou.
   - Po stisku klávesy F2 se otevře obrazovka, kde můžeš měnit úrovně svých
schopností a rychlost obnovování síly úderu. Na této obrazovce se zobrazují
jen ty schopnosti, které už máš. Jejich úroveň můžeš měnit pouze v rozsahu od 1
až po aktuálně odemčené maximum.
- V nastavení na kartě "Chování" bylo přidáno zaškrtávací políčko, které určuje,
jestli aktuálně zvolený způsob pohledu (z pozice postavy nebo ze středu hrací
plochy) zůstane zachován mezi jednotlivými hrami.
- Nyní je možné odstranit uložený postup hrou a obnovit výchozí nastavení.
   - Můžeš to udělat v nastavení na kartě "Obecné".
   - Pokud jsi do nastavení vstoupil/a z menu Pauza, obnovit nastavení ani vymazat
svůj postup nemůžeš.

### Změny

- Změnila se obrazovka pro výběr režimu hry.
   - obrazovka se nyní vykresluje ve virtuálním formuláři místo v menu. Navigace na
ní je podobná jako na obrazovce Nastavení nebo Profil.
   - Na nové obrazovce si můžeš vybrat, jestli se má hra nahrávat.
- Vylepšeno rozhraní obrazovky Profil.
   - Nyní lze libovolnou položku ze seznamu statistik zkopírovat do schránky
stisknutím kláves ctrl+C.
   - Na záložce Statistiky je nyní uvedeno, kolik máš aktuálně úspěchových bodů.
   - Aury nyní zobrazují i svůj bonus.
- Mírné změny ve vyvážení hry.
   - Za každých sto bodů až do tisíce dostaneš jednu minci. Například jsi získal/a
678 bodů, v takovém případě dostaneš 7 mincí a ne jednu jako dřív.
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
- Implementován režim pohledu z pozice postavy (pohled z první osoby). Chceš-li
režim přepnout, stiskni při hře klávesu V.
- Chyby při aktualizaci se nyní zapisují do souboru, který se nachází ve složce
userData/errorLogs.
- Přidány dočasné alternativní klávesy pro horizontální a vertikální máchnutí
pálkou.
   - Pro vodorovné máchnutí se teď používá klávesa e, pro svislé klávesa r.
   - Toto řešení je dočasné, jen do doby, než bude implementováno nastavení
vlastních klávesových zkratek.
- Položky v seznamu statistik, u kterých je dostupná odměna, jsou nyní na začátku
seznamu.

### Změny

- Zvýšen počet bodů za dokonalé trefy, odrazy míče od stropu a kolize míče s
předměty.
- Dokumentace byla aktualizována s ohledem na nové funkce.

### Opravy

- Zvýšena hlasitost zvuku při dopadu po výskoku.
- Aura vůdce nyní nezvyšuje počet bodů, o které přicházíš kvůli penalizacím.

## 1.0.0

První verze.
