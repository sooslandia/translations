% Lista promena

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
