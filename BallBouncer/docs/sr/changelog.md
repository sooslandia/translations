% Lista promena

## 1.3.2

### Ispravke

- Successful bat hit sound has been fixed and now plays in all intended
situations.
- Information on how to activate items has been added to the descriptions of
trial of will and trial of mastery modes.
- Fixed game crashes that occurred when a screen reader other than NVDA was
active.
- Potentially fixed a game crash that occurred when playing with recording
enabled.

## 1.3.1

Fixed a bug with objects sound panning.

## 1.3.0

This is the largest update, adding a lot of new content to the game.

Three new modes await you, each of which can be upgraded, along with the quest
board content featuring dozens of diverse quests. By completing these quests,
you can earn stars, which can then be spent on various upgrades.

New objects will help you score even more points than you could have ever
imagined.

New auras will breathe new life into your skills, while the new skills will open
up even more strategies for object destruction.

And of course, there are the upgrades that affect the entire gameplay, allowing
you to rack up points to unprecedented levels and create even more destruction
on the playing field.

To reach the true heights, you’ll have to spend dozens of hours, but don’t be
scared — those hours will be filled with unrestrained chaos of destruction and
the sweetness of well-deserved rewards!

### Nove funkcije

- New content added.
   - Three new modes, each with its own currency.
   - A quest board.
   - New statistics items.
   - New objects, skills, and auras, unlocked with the currencies of the new modes.
   - As well as many different upgrades that affect both the new modes and the
normal game.
- The ability to view the descriptions of game modes has been added.
   - To open the description, select a mode from the list on the new game start
screen and press the D key, or click the "Open Mode Description" button.

### Promene

- Now auras can be active or inactive.

   - Initially, you can use only two auras at the same time, but in the future, the
number of active auras can be increased, as well as new ones can be acquired.
   - You can also open the description of an aura, except for the leader and time
auras, by pressing the corresponding button on the auras tab in the profile.
- The "Furious leap" ability has been improved. Now the character can dash a
greater distance.
- The balance of points awarded for high streaks of collisions, object
destructions, and ball bounces off the ceiling has been adjusted.
- The upgrade cost for the Leader and Time auras has been increased. If your aura
level is above five, it will be reset to zero, and the achievement points
spent on upgrading it will be returned.
- Now you can activate menu items by pressing the Enter key on the numpad, and
also hold Enter on buttons for rapid activations.
- The calculation of the coin reward has been refined for final scores over two
million.
- The behavior of the sound playback for checking the character's position has
been changed.

   - Previously: The sound played at the character's position in the field center
view, and played at the center of the field in the first-person view.
   - Now: The sound always plays at the character's position, except when the
first-person view is active and ball watch mode is turned off. In this case,
the sound plays at the center of the field.
- The learn sounds screen has been redesigned.

   - The menu has been replaced with a virtual form.
   - Sounds, both from the base game and new modes, are now organized into separate
tabs of the form for easier navigation and the ability to listen to them
during gameplay.
- The method of recording gameplay has been changed.

   - Now, recordings are saved in MP3 format.
   - The old recording method has been disabled, but it is still possible to play
previously recorded files.
   - New recordings will be located in userData/mp3recordings.
   - The ability to play recordings in the old format will be removed in version
1.5.0.
- Minor changes and inconsistencies fixed in English translation.
- Setting skill levels in training mode has been fixed.

   - Now, changing skill levels will have an effect on the game session.
   - Also, now you can set any skill level up to the maximum possible.
- A critical bug has been fixed when changing controls configuration during
gameplay.
- The issue where the camera did not follow the character during a jump or when
using the "Furious leap" skill has been fixed.
- The accuracy of the character's hit on the ball when using the "Furious leap"
skill has been increased.
- Now, when the character jumps, the penalty timer for staying in one place is
reset.
- The issue that allowed opening the object map and pausing the game
simultaneously, leading to strange and undesirable behavior, has been fixed.
- The error in the calculation of points for object destruction has been fixed.
As a result, fewer points are now awarded for this.
- Incorrect setting of the skill cooldown time after an unsuccessful attempt has
been fixed.

## 1.2.4

### Ispravke

- Updated and corrected translations.

## 1.2.3

### Nove funkcije

- Dodati novi prevodi.
   - Srpski. Prevodilac [nidza07](https://github.com/nidza07).
   - Češki. Prevodilac [4sensegaming](https://github.com/4sensegaming).

### Ispravke

- Ispravljena sitna greška u turskom prevodu.
- Ispravljeno neispravno prikazivanje pomoći igre.
- Ispravljena potecijalna kritična greška kada se učitava snimak.

## 1.2.2

Ažurirani turski i indonežanski prevodi.

## 1.2.1

Ovo ažuriranje ispravlja nekoliko kritičnih grešaka za Linux korisnike.

## 1.2.0

Cilj ove verzije je da dodatno poboljša korisničko iskustvo i uredi postojeći
sadržaj. Sada možete da promenite tasterske prečice. Možete da snimite vašu igru
i reprodukujete snimke korišćenjem ugrađenog reproduktora snimaka. Dodata je
mapa objekata, kao i nekoliko drugih poboljšanja i ispravki.

Otvorili smo zvanični [github repozitorijum
prevoda](https://github.com/sooslandia/translations). Ako želite da prevedete
igru i imate mogućnost, rado ćemo prihvatiti vašu pomoć.

### Nove funkcije

- Dodati novi prevodi.
   - Turski. Prevodilac [fatihyuksek](https://github.com/fatihyuksek1).
   - Indonežanski. Prevodilac [MuhammadGagah](https://github.com/MuhammadGagah).
- Sada možete da promenite podrazumevane tasterske prečice.
   - Da biste to uradili, kliknite na dugme "Prilagodi tasterske prečice" koje se
nalazi na kartici "Podešavanje tasterskih prečica" u ekranu podešavanja.
   - Vaša datoteka sa podešavanjima se nalazi u folderu korisničkih podataka
(userData) i zove se keyConfig.json. Možete deliti vaša podešavanja sa drugim
ljudima. Kako bi tuđa podešavanja radila kod vas, morate da zamenite vašu
datoteku sa podešavanjima sa onom koju ste dobili od druge osobe.
   - Možete saznati više o podešavanjima u odgovarajućem delu dokumentacije.
- Sada možete da snimite vašu igru.
   - Možete da označite izborno polje koje određuje da li će vaša sesija igre biti
snimana na ažuriranom ekranu izbora režima. Ponašanje snimanja se može
podesiti na kartici snimanje na ekranu podešavanja.
   - Možete reprodukovati snimke iz menija snimaka, kojem možete pristupiti
aktiviranjem odgovarajuće stavke u glavnom meniju.
   - Snimci se čuvaju u recordings folderu, koji se nalazi u folderu vaših
korisničkih podataka (userData) i imaju .sgr ekstenziju. Datoteka snimka se
može preimenovati ako je neophodno i deliti sa drugim ljudima. Kako bi igra
prepoznala tuđi snimak, mora se prebaciti u folder snimaka.
   - Informacije o načinu rada reproduktora snimaka i njegovim prečicama se mogu
pronaći u odgovarajućem delu dokumentacije.
- Dodata mapa objekata.
   - Može se otvoriti tasterom m u toku igre.
   - Krećite se po mapi korišćenjem strelica. Možete takođe saznati koliko objekata
je na mapi pritiskanjem tastera o.
   - Postoje dva režima navigacije, o kojima možete pročitati više u odgovarajućem
delu dokumentacije.
   - Sve prečice mape objekata se mogu promeniti u podešavanjima tasterskih prečica.
- Režim vežbanja je takođe proširen.
   - Sada možete odmah oporaviti sve veštine tasterom f1.
   - Kada pritisnete taster f2, otvoriće se ekran na kojem možete da promenite nivoe
vaših veština i brzinu oporavka snage udarca. Ovaj ekran prikazuje samo
veštine koje imate. Možete promeniti njihov nivo samo u opsegu od nivoa 1 do
maksimalnog trenutnog nivoa.
- U podešavanjima, na kartici "ponašanje", dodato je izborno polje koje određuje
da li će se režim kamere čuvati između igara.
- Sada je moguće obrisati napredak igre i vratiti podešavanja na podrazumevana.
   - Ovo se može uraditi u podešavanjima, na kartici "opšta".
   - Nećete moći da vratite podešavanja ili obrišete napredak ako ste podešavanjima
pristupili iz menija pauze.

### Promene

- Ekran izbora režima igre je promenjen.
   - Ekran se sada prikazuje u obliku virtuelne forme umesto menija. Navigacija je
slična ekranima podešavanja i profila.
   - Sa novog ekrana možete odlučiti da li će igra biti snimljena.
- Poboljšan interfejs ekrana profila.
   - Sada se bilo koja stavka iz liste statistika može kopirati u privremenu
memoriju prečicom ctrl+c.
   - Kartica statistika sada prikazuje trenutni broj poena dostignuća.
   - Aure takođe prikazuju svoje bonuse.
- Sitne promene u balansu igre.
   - Sada na svakih sto poena do hiljadu, dobićete jedan novčić. Na primer, dobili
ste 678 poena, dobićete 7 novčića, a ne jedan kao ranije.
   - Nakon hiljadu poena, sve ostaje kao ranije, ali 10 novčića koje ste dobili vam
ostaju. Na primer, dobili ste 1234 poena, dobićete 11 novčića.
- Maksimalan broj objekata na terenu je povećan.
- Sada će zvuk koji se reprodukuje pritiskanjem tastera c u režimu kamere
fokusiranog na karaktera biti reprodukovan na centru terena.
- Format imena datoteke sa podacima o kritičnim greškama je promenjen na (error
gggg_MM_dd čč-mm-ss.log)

### Ispravke

- Sada, kada se prikazuju kritične greške, zvuk će u potpunosti biti isključen
umesto da se ponavlja.
- Poboljšana stabilnost igre u nekim situacijama.

## 1.1.1

### Ispravke

- Ispravljena kritična greška do koje je dolazilo kada su režim kamere fokusiran
na karaktera i režim gledanja loptice aktivirani u isto vreme.
- Ispravljene neke druge sitne greške.

## 1.1.0

Ova verzija se fokusira na poboljšanje korisničkog iskustva: Zvuk za uspešan
udarac palicom, režim kamere fokusiran na karaktera, alternativni tasteri za
udarac palicom, i tako dalje.

### Nove funkcije

- Igra sada podržava prevode kojima nedostaje jedan ili više nizova. Ako niz nije
pronađen, igra se vraća na nizove engleskog prevoda.
- U režimu gledanja loptice, dodat je pozadinski zvuk za plafon, što će gledanje
učiniti spektakularnijim.
- Dodat zvuk koji označava uspešan udarac loptice palicom. Podrazumevano,
obaveštenje je onemogućeno; može se omogućiti u podešavanjima, na kartici
"ponašanje".
- Dodat režim kamere fokusiran na karaktera. Da biste promenili režime,
pritisnite v u toku igre.
- Greške tokom ažuriranja se sada evidentiraju u datoteci koja će se nalaziti u
folderu userData/errorLogs.
- Dodati privremeni alternativni tasteri za horizontalne i vertikalne udarce
palicom.
   - Za horizontalni udarac, koristite taster e, za vertikalni udarac, koristite
taster r.
   - Ovo rešenje je privremeno i ostaje dok se ne doda podešavanje tasterskih
prečica.
- Sada su stavke sa dostupnom nagradom u listi statistika na početku liste.

### Promene

- Povećani poeni koji se dobijaju za nizove savršenih udaraca, odskakanja loptice
sa plafona i sudare loptice sa objektima.
- Dokumentacija je ažurirana kako bi se u obzir uzele nove funkcije.

### Ispravke

- Pojačan zvuk prizemljenja nakon skoka.
- Sada aura vođe ne povećava poene koji se gube usled kazni.

## 1.0.0

Prva verzija.
