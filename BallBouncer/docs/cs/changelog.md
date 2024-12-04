% Historie změn

## 1.2.2

Aktualizován turecký a indonéský překlad.

## 1.2.1

Tato aktualizace opravuje několik kritických chyb pro uživatele Linuxu.

## 1.2.0

Tato verze se zaměřuje na další vylepšování uživatelského prostředí a dolaďování
stávajícího obsahu. Nyní si můžete přiřadit klávesové zkratky podle vlastního
uvážení. Nyní je možné nahrávat své hraní a přehrávat výsledné nahrávky pomocí
vestavěného přehrávače těchto nahrávek. K dispozici je také mapa předmětů a
několik dalších vylepšení a oprav.

Otevřeli jsme oficiální překladový repozitář
[github](https://github.com/sooslandia/translations). Pokud chcete hru překládat
a máte na to schopnosti, rádi vaši pomoc přijmeme.

### Nové funkce

- Přidány nové překlady.
   - Turečtina. Překladatel [fatihyuksek](https://github.com/fatihyuksek1).
   - Indonéština. Překladatel [MuhammadGagah](https://github.com/MuhammadGagah).
- Nyní můžete změnit výchozí klávesové zkratky.
   - To provedete kliknutím na tlačítko "Nastavit klávesové zkratky", které najdete
na záložce "Nastavení klávesových zkratek" na obrazovce Nastavení.
   - Konfigurační soubor se nachází ve složce uživatelských dat (userData) a jmenuje
se keyConfig.json. Svou konfiguraci můžete sdílet s ostatními uživateli. Aby
vám konfigurace někoho jiného fungovala, musíte nahradit svůj konfigurační
soubor tím, který jste dostali od něj.
   - Více informací o nastavení klávesových zkratek najdete v příslušné části
dokumentace.
- Nyní můžete nahrávat své hraní.
   - Na aktualizované obrazovce pro výběr režimu hry můžete zaškrtnout políčko,
které určuje, jestli se vaše hraní má nahrávat. Chování nahrávání lze
nakonfigurovat na záložce Nahrávání na obrazovce Nastavení.
   - Nahrávky můžete poslouchat v menu Nahrávky, do kterého se dostanete příslušnou
položkou hlavního menu.
   - Nahrávky se ukládají do složky nahrávky (Recordings), která se nachází ve
složce uživatelských dat (userData), a mají příponu .sgr. Soubor s nahrávkou
lze v případě potřeby přejmenovat a sdílet s dalšími lidmi. Aby hra rozpoznala
nahrávku někoho jiného, musí být umístěna v příslušné složce s nahrávkami.
   - Informace o tom, jak přehrávač nahrávek funguje, a o jeho ovládacích tlačítkách
najdete v příslušné části dokumentace.
- Přidána mapa předmětů.
   - Během hraní ji lze otevřít klávesou m.
   - Pohybujte se po mapě pomocí šipek. Stisknutím klávesy o můžete také zjistit,
kolik předmětů se na mapě nachází.
   - Existují dva režimy pohybu kurzoru, o kterých se dočtete v příslušné části
dokumentace.
   - Všechny klávesové zkratky pro mapu předmětů lze změnit v konfiguraci
klávesových zkratek.
- Vylepšen je také režim tréninku.
   - Stisknutím klávesy f1 nyní můžete okamžitě vynulovat prodlevu před dalším
použitím u všech schopností.
   - Po stisku klávesy f2 se otevře obrazovka, kde můžete měnit úrovně svých
schopností a rychlost obnovení síly úderu. Na této obrazovce se zobrazují jen
ty schopnosti, které už máte. Jejich úroveň můžete měnit pouze v rozsahu od
úrovně 1 až po aktuální maximum.
- V nastavení na kartě "Chování" bylo přidáno zaškrtávací políčko, které určuje,
jestli aktuálně zvolený způsob pohledu (z pozice postavy nebo ze středu hrací
plochy) zůstane zachován mezi jednotlivými hrami.
- Nyní je možné odstranit uložený postup hrou a obnovit výchozí nastavení.
   - Můžete to udělat v nastavení na kartě "Obecné".
   - Pokud jste do nastavení vstoupili z menu Pauza, obnovit nastavení ani vymazat
svůj postup nemůžete.

### Historie změn

- Změnila se obrazovka pro výběr režimu hry.
   - obrazovka se nyní vykresluje ve virtuálním formuláři místo v menu. Navigace na
ní je podobná jako na obrazovce Nastavení nebo Profil.
   - Na nové obrazovce můžete určit, jestli se má hra nahrávat.
- Vylepšeno rozhraní obrazovky Profil.
   - Nyní lze libovolnou položku ze seznamu statistik zkopírovat do schránky
stisknutím kláves ctrl+c.
   - Na záložce Statistiky je nyní uvedeno, kolik aktuálně máte úspěchových bodů.
   - Aury nyní zobrazují i svůj bonus.
- Mírné změny ve vyvážení hry.
   - Za každých sto bodů až do tisíce získáte jednu minci. Například jste získali
678 bodů, v takovém případě obdržíte 7 mincí, a ne jednu jako dříve.
   - Až se dostanete na tisíc bodů, zůstává vše při starém, ale těch prvních 10
mincí, které jste získali předtím, máte pořád. Například jste získali 1234
bodů, v takovém případě obdržíte 11 mincí.
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

Tato verze se zaměřuje na zlepšení uživatelského zážitku: Zvuk při trefě pálkou
do míče, režim pohledu z pozice postavy, alternativní klávesy pro máchnutí
pálkou atd.

### Nové funkce

- Hra nyní podporuje překlady, ve kterých chybí jeden nebo více řetězců. Pokud
není řetězec nalezen, hra se vrátí k anglickým lokalizačním řetězcům.
- V režimu sledování míče nyní strop přehrává zvuk na pozadí, takže sledování teď
bude efektnější.
- Přidán zvuk, který signalizuje úspěšnou trefu pálkou do míče. Ve výchozím
nastavení je toto upozornění vypnuté; můžete si ho zapnout v nastavení na
kartě "Chování".
- Implementován režim pohledu z pozice postavy (pohled z první osoby). Chcete-li
režim přepnout, stiskněte při hře klávesu V.
- Chyby při aktualizaci se nyní zapisují do souboru, který se nachází ve složce
userData/errorLogs.
- Přidány dočasné alternativní klávesy pro horizontální a vertikální máchnutí
pálkou.
   - Pro vodorovné máchnutí použijte klávesu e, pro svislé klávesu r.
   - Toto řešení je dočasné, jen do doby, než bude implementováno nastavení
vlastních klávesových zkratek.
- Položky v seznamu statistik, u kterých je dostupná odměna, jsou nyní na začátku
seznamu.

### Historie změn

- Zvýšen počet bodů za dokonalé trefy, odrazy míče od stropu a kolize míče s
předměty.
- Dokumentace byla aktualizována s ohledem na nové funkce.

### Opravy

- Zvýšena hlasitost zvuku při dopadu po výskoku.
- Aura vůdce nyní nezvyšuje počet bodů, o které přijdete kvůli penalizacím.

## 1.0.0

První verze.
