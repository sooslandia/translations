% Lista promena

## 1.4.2

### Promene

- Ažurirani prevodi.
   - Srpski. Prevodilac [nidza07](https://github.com/nidza07).
   - Turski. Prevodilac [fatihyuksek](https://github.com/fatihyuksek1).
   - Češki. Prevodilac [4sensegaming](https://github.com/4sensegaming).

### Ispravke

- Ispravljeno rano pojavljivanje kartica zvezdanih modula i druga poboljšanja
prodavnice.
- Ispravljena reprodukcija duplog zvuka kada se aktivira dugme da na ekranu
ažuriranja.

## 1.4.1

Ispravljena kritična greška kada se otvori profil.

## 1.4.0

Ova verzija ispravlja brojne postojeće probleme, kao što su izuzetna kompleksnost
režima probe majstora, težina pri pronalasku i aktiviranju predmeta, nedostatak
praćenja statistika završenih misija i otvorenih kovčega, nemogućnost
prepoznavanja kada veština "besni skok" može da se aktivira, i još toga.

Takođe su dodata nova pojačanja, i izvršena poboljšanja balansa statistika
jubileja.

Rešen je problem opterećenja zvučnog sistema, što je dovelo do povećanja broja
osvojenih poena.

### Nove funkcije

- Nagrada za završene misije se sada može povećati.
   - Da pristupite novom ekranu, aktivirajte dugme "Povećanje nagrade za završene
misije" koje se nalazi na kartici table misija na vašem profilu.
   - Povećanje se vrši novčićima, zelenim, plavim i crvenim kuglicama.
   - Svaka valuta ima svoje odvojeno poboljšanje, ali sve one zajedno utiču na jedan
parametar: šansu da dobijete dodatnu zvezdu.
   - Ako šansa da dobijede dodatnu zvezdu dostigne 100%, garantovano je da ćete
dobiti jednu dodatnu zvezdu i nagradu, i brojač šanse će se resetovati.
- Režim probe majstora je dobio sitne promene.
   - Loptice više ne mogu da se sudare jedna sa drugom.
   - Minimalan broj objekata na terenu je povećan.
   - Odskakanje loptica sa platfona sada započinje niz koji vam donosi određeni broj
poena.
   - Dodati su savršeni udarci.
      - Da izvršite savršen udarac u režimu probe majstora, udarite lopticu palicom
kada je snaga vašeg udarca u potpunosti oporavljena.
      - Ako promašite ili ne udarite lopticu punom snagom, niiz će se resetovati.
      - Nizovi i savršeni udarci se beleže u statistikama.
   - Bonus smanjenja kazne za odskakanje loptice je promenjen sa 2% na 5% po nivou.
   - Opis režima je ažuriran kako bi ste se upoznali sa izvršenim promenama.
- Muzika glavnog menija je ažurirana.
   - Sada možete bezbedno da podelite video ili audio snimke igre bez isključivanja
muzike.
   - Ogromna zahvalnost korisniku [Nikita K](https://t.me/NikitaKOfficial) za njegov
naporan rad!
- Dodat je zvuk koji vas obaveštava kada je misija završena.
- Dodato je novo pojačanje koje povećava bonus za izbegavanje električnih
pražnjenja u režimu probe brzine.
- Dodata su nova zvezdana pojačanja.
   - Povećano trajanje nizova uništenja, sudara i odskakanja od plafona.
   - Podrška mirnoće.
- Sada možete da saznate koliko visoko je loptica.
   - Podrazumevani taster ove funkcije je B.
   - Kada se iskoristi, čućete informaciju koliko visoko se loptica nalazi, kao i
poseban zvuk koji se reprodukuje na trenutnoj visini loptice.
   - U režimu probe majstora, pozicija svih loptica na terenu će biti izgovorena po
redu, a zvuk će se reprodukovati na visini najniže loptice.
- Dodate su nove stavke statistika.
   - Ukupan broj otvorenih kovčega.
   - Ukupan broj završenih misija.
- Dodato je prilagođavanje balansa zvuka.
   - Da pristupite ovom ekranu, pritisnite odgovarajuće dugme na ekranu podešavanja,
na kartici "Zvuk".
   - Kako biste dobili pomoć za ovu funkciju, pritisnite dugme "pomoć" na ekranu
podešavanja balansa zvuka.
- Sada možete da onemogućite pravljenje mina, kauča i kutija za alat na terenu.
   - Dodata je lista izbornih polja na ekranu izbora režima, koja vam dozvoljava da
uključite ili isključite pravljenje određenih objekata.
   - Lista će biti skrivena ako je kursor izbora režima podešen na bilo koji drugi
režim osim standardnog i vežbanja.
- Dodata je funkcija koja vam dozvoljava da se prebacite između veština koje su
spremne za korišćenje.
   - Prebaci se na sledeću veštinu koja je spremna za korišćenje: taster jednako (=)
ili numerički minus (-).
   - Prebaci se na sledeću veštinu koja je spremna za korišćenje: taster crtica (-)
ili numerički taster puta (*).
   - Tasteri se primenjuju sa podrazumevanim podešavanjima kontrolama.
- Dodato je novo podešavanje koje vam dozvoljava da onemogućite odbrojavanje pre
početka igre.
- Dodata je funkcija koja vam dozvoljava da brzo promenite zvuk loptice.
   - Da promenite zvuk, uđite u režim gledanja loptice tokom igre, a zatim
pritisnite taster L da kružite između zvukova.
   - U režimu probe majstora, ova funkcija radi na sličan način. Koristite taster J
da izaberete lopticu čiji zvuk želite da promenite, a zatim pritisnite taster
L.
   - Pritiskanjem tastera F1 tokom igre režima probe majstora, otvorićete ekran
prilagođavanja zvuka loptice, gde možete da promenite zvukove u mirnom
okruženju.
      - Ekran sadrži četiri elementa: tri liste, svaka odgovara određenoj loptici, i
dugme za zatvaranje ekrana.
      - Da čujete zvuk loptice, pritisnite Enter ili Razmak na bilo kom zvuku u listi.
      - Možete prekinuti reprodukciju zvuka navigacijom po listi ili ekranu.
   - Izabrani zvukovi se čuvaju između igara.
- Dodato je podešavanje koje vam dozvoljava da normalizujete visinu svih zvukova
loptica na približno isti nivo.
   - Kada puštate zvukove na ekranu menjanja zvuka loptice, reprodukuju se na istoj
visini. Ali, tokom igre, zvukovi osim prvog se ne podudaraju u potpunosti po
visini.
   - Bez obzira na ovo, funkcija može biti korisna za one koji koriste zvukove
loptice osim prvog i imaju problema da razlikuju zvukove u bučnim okruženjima,
budući da povećanje visine takođe povećava zvučnost.
- Dodato je novo podešavanje koje vam dozvoljava da se prebacite u režim gledanja
loptice pritiskanjem jednog tastera umesto da držite taster.
- Meni pauze sada uključuje opciju gledanja veštine koje su podešene na mesta
(meni "aktivne veštine").

### Promene

- Sada, u režimima probe volje i majstora, ako ste blizu predmeta i možete da ga
aktivirate, visina zvuka predmeta će biti blago povišena.
- Kazna za odskakanje loptice od poda je promenjena.
   - ako loptica odskoči od poda 40 puta zaredom, kazna za naredna odskakanja će se
veoma brzo povećavati.
   - Ova promena je izazvana novim pojačanjem "podrška mirnoće".
- Nagrada za otvaranje kovčega sreće je povećana.
- Izvršene su određene promene u nagradama za dostizanje statističkih jubileja.
Ako se prepoznaju bilo koji nedostaci kada se igra pokrene, prethodno
dodeljeni poeni dostignuća će biti resetovani i nagrade će biti ponovo
izračunate.
- U režimima probe volje i majstora, ista vrsta predmeta se više ne može pojaviti
više od dva puta zaredom.
- U režimu probe brzine, isti efekat se više ne može pojaviti dva puta zaredom.
- Promene u prodavnici: vremenska aura i aura vođe su prebačene na karticu
"aure"; "povećanje šanse pojavljivanja posebnih objekata" pojačanje je
prebačeno na "karticu "objekti".
- Nagrade za manje rezultate u režimima probe su povećane.
- Efekat pojačanja koje povećava broj dobijenih crvenih kugli je poboljšan.
- Računanje nagrade novčića je poboljšano za ukupne rezultate iznad 100 miliona.
- Ako ste kupili maksimalan broj mesta za misije, dugme za kupovinu će sada biti
skriveno sa ekrana.
- Veština "besni skok" je poboljšana. Sada karakter može da se zaleti i kada je
udaljenost veća.
- Prikazivanje liste nagrada koja se prikazuje kada se otvori više kovčega sreće
odjednom je ažurirana.

### Ispravke

- Obrađivanje reprodukcije velikog broja zvukova u isto vreme je poboljšano.
   - Kao rezultat ove optimizacije, ukupan broj zvukova tokom uništenja objekata je
smanjen. Ali, zvučno okruženje još uvek može biti preopterećeno.
   - Možete takođe primetiti da dobijate značajnije više poena tokom igranja
standardnog režima. Ovo je očekivano i događa se zbog toga što je ogromno
opterećenje zvučnog sistema —koje je ranije izazivalo usporavanje igre —rešeno.
- Ispravljeno retko zamrzavanje i rušenje koje se događalo odmah nakon što
započnete igru kada je snimanje igre omogućeno.
- Ispravljena greška zbog koje dobijanje bonusa za uništenje lutke ili
izbegavanje električnog pražnjenja može povećati negativan rezultat.
- Ispravljeno neispravno ponašanje koje se događalo kada koristite veštinu "besni
skok".
- Napredak za misiju "Udarite plafon lopticom dok je efekat nematerijalnosti
aktivan" se sada takođe računa kada se koristi zvezdani modul "kontroler
loptice".
- Poboljšano obrađivanje ažuriranje vremena resetovanja misija i kovčega.
- Opisi nekih pojačanja u prodavnici su prošireni.
- Sada možete da preskočite animaciju za dobijanje novčića i drugih valuta
tasterom Enter na numeričkoj tastaturi.

## 1.3.5

### Promene

- Ažurirani prevodi.
   - Srpski. Prevodilac [nidza07](https://github.com/nidza07).
   - Turski. Prevodilac [fatihyuksek](https://github.com/fatihyuksek1).
- Izmenjen kriterijum završavanja nekih misija.
- Sada, ako je režim gledanja loptice omogućen, kazna za stajanje u mestu se ne
primenjuje.

### Ispravke

- Ispravljena mogućnost korišćenja određenih aura ako nisu aktivne.
- Aura s' onog sveta je promenjena tako da je sada lakše udariti lopticu palicom.
- Ispravljeno ponašanje električnih punjenja u režimu probe brzine, gde su mogla
da udare karaktera i da se računaju kao da su u isto vreme udarila zemlju.
- Ispravljena kritična greška kada se koriste veštine "magnetizam" i "raketna
salva" u isto vreme.
- Ispravljena kritična greška kada se koriste veštine "hvatalačka duša" i "besni
skok" u isto vreme.
- Verovatno ispravljena kritična greška do koje je dolazilo kada se igrica
restartuje nakon ažuriranja.
- Ispravljena reprodukcija zvukova za obaveštenje o nizu sudara sa objektima.

## 1.3.4

### Promene

- Ažuriran češki prevod.
Prevodilac[4sensegaming](https://github.com/4sensegaming).
- Ažuriran španski prevod. Prevodilac: [ogomez92](https://github.com/ogomez92).
- Ako ne možete da aktivirate auru, dobićete jasno obaveštenje.
- Ako nemate dovoljno energije da aktivirate zvezdani modul, dobićete obaveštenje
kada pokušate da ga aktivirate.

### Ispravke

- Ispravljen problem uz zdsr.
- Ponašanje gola u režimu probe brzine je ispravljeno.
   - Sada se gol spušta nazad na originalnu visinu nakon što se završi efekat lifta.
   - Gol više neće nestajati sa mape objekata kada se podiže ili spušta.
- Ispravljeno praćenje završetka određenih misija u režimu vežbanja.

## 1.3.3

### Nove funkcije

- Dodat španski prevod. Prevodioci:
[rayo-alcantar](https://github.com/rayo-alcantar),
[ogomez92](https://github.com/ogomez92).

### Promene

- Ažuriran češki prevod.
Prevodilac[4sensegaming](https://github.com/4sensegaming).

### Ispravke

- Ispravljena kritična greška do koje je dolazilo kada se puno zvukova
reprodukovalo u isto vreme.
- Ispravljeni problemi sa zvezdanim modulima.
   - Kartica dodatnih informacija modula se sada ažurira kada kupujete pojačanja.
   - Opis pojačanja povećanja brzine modula kontrolera loptice više ne uključuje
informacije o povećanju brzine od dvanaest posto.
   - Kada se pritisne taster za proveru trenutne zvezdane energije, broj se sada
izgovara na početku poruke.
   - Ispravljena kritična greška kada se aktivira zvezdani modul "kontroler loptice"
i loptica uhvati u toku aktivacije.
- Ispravljeno praćenje završetka misije korišćenja veštine magnetizma u režimu
vežbanja.
- Ispravljeni problemi sa snimanjem.
   - Kada se igra zatvori prečicom Alt+F4 u toku igre, snimanje se prekida ako se
označi opcija "Otkaži snimak pri ručnom prekidanju igre" i uspešno završava
ako ova opcija nije označena.
   - Kada se igra završi pre vremena zbog rezultata od -1000 poena, snimanje se više
ne prekida čak i kada je opcija "Otkaži snimak pri ručnom prekidanju igre"
označena.
- Sada je moguće igrati uz JAWS.
- Ispravljena greška pri pokretanju igre na Windowsu za neke korisnike.

## 1.3.2

### Ispravke

- Zvuk za uspešan udarac palicom je ispravljen i sada se reprodukuje u svim
željenim situacijama.
- Informacije kako se predmeti aktiviraju su dodate u opise režima probe volje i
probe majstora.
- Ispravljeno rušenje igre do kog je dolazilo kada je neki drugi čitač ekrana
koji nije NVDA aktivan.
- Problemi sa MP3 snimcima su ispravljeni.
   - Potencijalno ispravljeno rušenje igrice do kojeg je dolazilo prilikom igranja
uz omogućeno snimanje.
   - Posebno VBR zaglavlje je dodato u snimke. Ranije, odsustvo ovog zaglavlja je
izazvalo da neki reproduktori neispravno prikazuju trajanje snimka i imaju
probleme sa premotavanjem.
   - MP3 parametri kodiranja su promenjeni kako bi se smanjila veličina datoteke bez
značajnog gubitka kvaliteta.-
- Dodat je red u dokumentaciju koji objašnjava kako se otključava tabla misija (u
sekciji "Drugi režimi igre").
- Ispravljena kritična greška do koje je dolazilo kada se puno zvukova
reprodukovalo u isto vreme.

## 1.3.1

Ispravljena greška sa pozicioniranjem zvukova objekata.

## 1.3.0

Ovo je najveće ažuriranje, dodajući puno novog sadržaja u igricu.

Tri nova režima vas čekaju, svaki od njih se može pojačati, uz tablu misija koja
sadrži desetine raznovrsnih misija. Završavanjem ovih misija, možete da zaradite
zvezde, koje se zatim mogu potrošiti na različita pojačanja.

Novi objekti će vam pomoći da dobijete čak i više poena nego što ste ikada
zamislili.

Nove aure će oživeti vaše veštine, dok će nove veštine otvoriti još više
strategija za uništavanje objekata.

I naravno, tu su pojačanja koja utiču na celu igru, dozvoljavajući vam da
povećate poene na do sad neviđene nivoe i pravite još veću destruktivnost na
terenu.

Da dostignete istinske visine, moraćete da provedete desetine sati, ali ne
plašite se — ti sati će biti popunjeni neograničenim haosom uništenja i
slatkoćom dobro zasluženih nagrada!

### Nove funkcije

- Dodat novi sadržaj.Dodati novi prevodi.
   - Tri nova režima, svaki sa svojom sopstvenom valutom.
   - Tabla misija.
   - Nove stavke statistika.
   - Novi objekti, veštine i aure, otključavaju se valutama novih režima.
   - Kao i puno različitih pojačanja koja utiču i na nove režime i na standardnu
igru.
- Dodata je mogućnost gledanja opisa režima igre.
   - Da otvorite opis, izaberite režim iz liste na novom ekranu za početak igre i
pritisnite taster D, ili aktivirajte dugme "Otvori opis režima".

### Promene

- Aure sada mogu biti aktivne i neaktivne.
   - Na početku, možete koristiti samo dve aure u isto vreme, ali u budućnosti, broj
aktivnih aura se može povećati, a nove se mogu nabaviti.
   - Možete takođe otvoriti opis aure, osim za auru vođe i vremensku auru,
aktiviranjem odgovarajućeg dugmeta na kartici aura na profilu.
- Veština "besni skok" je poboljšana. Sada karakter može da se zaleti i kada je
udaljenost veća.
- Balans poena koji se dobijaju za veće nizove sudara, uništenja objekata, i
odskakanja loptice sa plafona je promenjen.
- Cena pojačanja za vremensku auru i auru vođe je povećana. Ako je vaš nivo aure
iznad pet, biće vraćen na nulu, a poeni dostignuća koje ste potrošili da je
pojačate će biti vraćeni.
- Sada možete da aktivirate stavke menija pritiskanjem numeričkog tastera Enter,
i takođe da držite Enter na dugmićima za bržu aktivaciju.
- Računanje nagrade novčića je poboljšano za konačne rezultate iznad dva miliona.
- Ponašanje reprodukcije zvuka za proveru pozicije karaktera je promenjeno.
   - Ranije: Zvuk se reprodukovao na poziciji karaktera sa kamerom fokusiranom na
teren, a reprodukovao se na centru terena sa kamerom fokusiranom na karaktera.
   - Sada: Zvuk se uvek reprodukuje na poziciji karaktera, osim kada je perspektiva
fokusirana na karaktera aktivna a režim gledanja loptice je onemogućen. In
this case, the sound plays at the center of the field.
- Ekran učenja zvukova je redizajniran.
   - Meni je zamenjen virtuelnom formom.
   - Zvukovi iz standardne igre ali i iz drugih režima su sada organizovani po
odvojenim karticama forme radi lakše navigacije i kako biste mogli da ih
čujete u toku igre.
- The Metod snimanja igre je promenjen.
   - Snimci se sada čuvaju u MP3 formatu.
   - Stari način snimanja je onemogućen, ali je reprodukovanje prethodno snimljenih
datoteka još uvek moguće.
   - Novi snimci će se nalaziti u folderu userData/mp3recordings.
   - Mogućnost reprodukcije snimaka u starom formatu će biti uklonjena u verziji
1.5.0.
- Sitnije promene i ispravke nedoslednosti u engleskom prevodu.
- Podešavanje nivoa veština u režimu vežbanja je ispravljeno.
   - Sada, menjanje nivoa veština će imati uticaj na trenutnu igru.
   - Takođe, sada možete da podesite nivo bilo koje veštine na maksimalan.
- Ispravljena je kritična greška kada se menjaju podešavanja kontrola u toku igre.
- Ispravljena je greška zbog koje kamera nije pratila karaktera tokom skoka ili
kada se koristi veština "besni skok".
- Preciznost udarca loptice kada se koristi veština "besni skok" je povećana.
- Sada, kada karakter skoči, vreme za kaznu stajanja u mestu se resetuje.
- Greška koja je dozvoljavala otvaranje mape objekata i u isto vreme pauziranje
igre, a nakon toga čudno i neželjeno ponašanje, je ispravljena.
- Greška pri računanju poena za uništenje objekata je ispravljena. Kao rezultat
toga, za ovo se sada dobija manje poena.
- Neispravno postavljanje vremena oporavka veštine nakon neuspešnog korišćenja je
ispravljeno.

## 1.2.4

### Ispravke

- Ažurirani i ispravljeni prevodi.

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
   - ekran se sada prikazuje u obliku virtuelne forme umesto menija. Navigacija je
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
