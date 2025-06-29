% değişiklik günlüğü

## 1.4.0

This release addresses numerous existing issues, such as the overly complex trial
of mastery mode, difficulties in identifying and activating items, the lack of
stat tracking for completed quests and opened chests, the inability to determine
when the "Furious leap" skill can be activated, and more.

New upgrades have also been added, and statistics milestone reward balancing has
been carried out.

High load on the audio system was resolved, which led to an increase in the
points scored.

### Yeni özellikler

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

### Değişiklikler

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
- "Öfkeli sıçrama" yeteneği iyileştirildi.  Şimdi oyuncu daha fazla mesafe
koşabiliyor.
- The display of the rewards list shown when opening multiple Luck Chests at once
has been updated.

### Düzeltmeler

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

### Değişiklikler

- Çeviriler güncellendi.
   - Sırpça. Çevirmen [nidza07](https://github.com/nidza07).
   - Türkçe. Çevirmen [fatihyuksek](https://github.com/fatihyuksek1).
- Bazı görevler için tamamlama kriterleri değiştirildi.
- Top izleme modu etkinken oyuncu aynı yerde durursa artık ceza uygulanmıyor.

### Düzeltmeler

- Etkin değil iseler bazı auraları kullanabilme durumu düzeltildi.
- Uhrevi aura, topa daha kolay vurulmasını sağlayacak şekilde değiştirildi.
- Hız denemesi modundaki elektrik akımının karaktere vurursa aynı zamanda yere
vuruyor sayıldığı bir davranış düzeltildi.
- Manyetizma ve roket salvosu becerilerini aynı anda kullanırken kritik hata
düzeltildi.
- Yakalayıcının ruhu ve öfkeli sıçrayış becerilerini aynı anda kullanırken kritik
hata düzeltildi.
- Oyun güncellemeden sonra başlatıldığında kritik hata alma sorunu bir ihtimal
düzeltildi.
- Nesne çarpışma serisi bildirim sesi için ses oynatma düzeltildi.

## 1.3.4

### Değişiklikler

- Çekçe çeviri güncellendi. Çevirmen
[4sensegaming](https://github.com/4sensegaming).
- İspanyolca çeviri güncellendi. Çevirmen:
[ogomez92](https://github.com/ogomez92).
- Bir aurayı etkinleştiremiyorsanız, artık net bir şekilde bilgilendirileceksiniz.
- Bir yıldız modülünü etkinleştirmek için yeterli enerjiniz yoksa,
etkinleştirmeye çalışırken bildirim alacaksınız.

### Düzeltmeler

- Zdsr ile ilgili bir sorun düzeltildi.
- Hız denemesi modunda kalenin davranışı düzeltildi.
   - Yükseltici etkisi bittikten sonra  kale orijinal boyutuna geri dönüyor.
   - Kale, inerken veya çıkarken nesne haritasından kaybolmayacak.
- Antrenman modunda belli görevlerin tamamlanmasının izlenmesi düzeltildi.

## 1.3.3

### Yeni özellikler

- İspanyolca çeviri eklendi. Çevirmenler:
[rayo-alcantar](https://github.com/rayo-alcantar),
[ogomez92](https://github.com/ogomez92).

### Değişiklikler

- Çekçe çeviri güncellendi. Çevirmen
[4sensegaming](https://github.com/4sensegaming).

### Düzeltmeler

- Birçok ses aynı anda çalarken kritik bir hata düzeltildi.
- Yıldız modülleri ile ilgili sorunlar düzeltildi.
   - Yükseltme aldığınızda, ek modül bilgisi sekmesi  güncelleniyor.
   - "Top kumandası" modülünün top hızını artırması açıklamasında  yüzde on iki hız
artışı bilgisi artık yer almıyor.
   - Mevcut yıldız enerjisi miktarını kontrol etme tuşuna basıldığında, enerji
sayısı  artık mesajın başında bildiriliyor.
   - "Top kumandası" modülünü etkinleştirilirken ve top yakalandığında kritik bir
hata düzeltildi.
- Antrenman modunda "manyetizma" becerisinin kullanılması görevinin izlenmesi
düzeltildi.
- Kayıt sorunları düzeltildi.
   - Oyun esnasında oyun alt+f4 ile kapatıldığında, "oyun el ile sonlandırıldığında
kaydı iptal et" onay kutusu işaretli ise kayıt iptal edilir, işaretli değilse
kayıt düzgün şekilde sonlandırılır.
   - -1000 puana ulaşıldığı için oyun erken sona erdiğinde, "Oyunu el ile
sonlandırırken kaydı iptal et" onay kutusu işaretli olsa bile kayıt  iptal
edilmez.
- JAWS açıkken oyun oynanabiliyor.
- Bazı kullanıcılar için Windows'ta oyunu başlatırken oluşan bir sorun düzeltildi.

## 1.3.2

### Düzeltmeler

- Başarılı sopa vuruşu sesi düzeltildi ve artık amaçlanan tüm durumlarda çalıyor.
- Ustalık denemesi ve irade denemesi modlarında öğelerin etkinleştirilme bilgisi
modların açıklamalarına eklendi.
- NVDA'dan başka bir ekran okuyucu etkinken oyunun çökme sorunu düzeltildi.
- Mp3 kayıtları ile ilgili sorunlar düzeltildi.
   - Kayıt etkinleştirildiğinde oyunu oynarken potansiyel çökme düzeltildi.
   - Kayıtlara özel VBR başlığı eklendi. Önceden, VBR başlığının olmaması bazı
oyuncuların kaydın süresini yanlış görmesine ve ileri/geri sarma ile ilgili
sorunlara neden oluyordu.
   - Mp3 şifreleme parametreleri, belirgin kalite kaybı olmadan dosya boyutunu
küçültecek şekilde ayarlandı.-
- Kılavuza görev panosunun nasıl açılacağını açıklayan bir satır eklendi (Diğer
Oyun Modları bölümünde).
- Birçok ses aynı anda çalarken kritik bir hata düzeltildi.

## 1.3.1

Nesne seslerinin yaslanması ile ilgili bir hata düzeltildi.

## 1.3.0

Bu, oyuna çok sayıda yeni içerik ekleyen en büyük güncellemedir.

Her biri yükseltilebilen üç yeni mod ve onlarca farklı görev içeren görev panosu
içeriği sizi bekliyor. Bu görevleri tamamlayarak yıldız kazanabilir ve bu
yıldızları çeşitli yükseltmelerde kullanabilirsiniz.

Yeni nesneler, önceden hayal bile edebileceğinizden daha fazla puan kazanmanıza
yardımcı oluyor.

Yeni auralar becerilerinize yeni bir soluk üfleyecek, yeni beceriler ise daha
fazla nesneyi yok etmek için yeni stratejiler ortaya çıkaracak.

Ve tabii ki, tüm oyunu etkileyen, puanlarınızı eşi benzeri görülmemiş seviyelere
çıkarmanızı ve oyun sahasında daha da fazla yıkım oluşturmanızı sağlayan
yükseltmeler de mevcut.

Gerçek zirvelere ulaşmak için onlarca saat harcamak zorunda kalacaksınız, ancak
korkmayın - bu saatler sınırsız yok etme dolu kaos ve hak edilmiş ödüllerin
tatlılığı ile dolu olacak!

### Yeni özellikler

- Yeni içerik eklendi.
   - Her biri kendine özgü para birimi olan üç yeni mod eklendi.
   - Görev panosu.
   - Yeni istatistik öğeleri.
   - Yeni modların para birimleriyle kilidi açılan yeni nesneler, beceriler ve
auralar.
   - Bunun yanısıra, hem yeni modları hem de normal modu etkileyen çok çeşitli
beceriler.
- Oyun modlarının açıklamalarını görüntüleyebilme özelliği eklendi.
   - Açıklamayı açmak için, yeni oyun başlat ekranındaki listeden modu seçip D
tuşuna basın veya "mod açıklamasını aç" düğmesine tıklayın.

### Değişiklikler

- Auralar etkin veya devre dışı olabiliyor.
   - Başlangıçta, aynı anda sadece iki aura kullanabilirsiniz, fakat gelecekte,
aktif aura sayısı artırılabilir ve yeni auralar elde edilebilir.
   - Ayrıca, profilinizdeki auralar sekmesinde ilgili düğmeye basarak, lider ve
zaman auraları dışında bir auranın açıklamasını da açabilirsiniz.
- "Öfkeli sıçrama" yeteneği iyileştirildi.  Şimdi oyuncu daha fazla mesafe
koşabiliyor.
- Yüksek çarpışma, nesne yok etme ve tavandan seken top serileri için verilen
puan dengesi ayarlandı.
- Lider ve zaman auraları için yükseltme bedeli artırıldı. Aura seviyeniz beşin
üzerindeyse, sıfıra sıfırlanacak ve yükseltme için harcanan başarı puanları
geri verilecek.
- Menü öğelerini numaratördeki enter tuşu ile etkinleştirebilir ve düğmeleri
hızlıca etkinleştirmek için enter tuşunu basılı tutabilirsiniz.
- İki milyonun üzerindeki puanlar için para ödülünün hesaplanması iyileştirildi.
- Oyuncunun pozisyonunu kontrol etmek için sesin oynatılma davranışı değiştirildi.
   - Önceden; ses saha ortasında modundayken oyuncunun olduğu yerden; birinci şahıs
modunda ise sahanın ortasından çalınıyordu.
   - Şimdi ise Birinci şahıs modu etkin ve top izleme modu kapalı olması hariç tüm
durumlarda, ses her zaman oyuncunun bulunduğu yerde çalıyor. Aksi takdirde,
ses sahanın merkezinden çalıyor.
- Sesleri öğrenme ekranı yeniden tasarlandı.
   - Menü, sanal bir form ile değiştirildi.
   - Hem temel oyun hem de yeni modların sesleri, daha kolay gezinme ve oyun
sırasında bunları dinleme olanağı için  formun ayrı sekmelerinde toplandı.
- Oyunu kaydetme yöntemi değiştirildi.
   - Kayıtlar mp3 formatında kaydediliyor.
   - Eski kayıt yöntemi devre dışı bırakıldı, ancak hala önceden çalınan dosyalar
oynatılabilir.
   - Yeni kayıtlar, userData/mp3recordings klasöründe bulunabilir.
   - Eski formattaki kayıtları oynatma özelliği 1.5.0 sürümünde kaldırılacak.
- İngilizce çeviride küçük değişiklikler yapıldı ve tutarsızlıklar düzeltildi.
- Antrenman modunda beceri seviyelerini ayarlama düzeltildi.
   - Beceri seviyelerini değiştirmek oyun oturumunu etkileyecek.
   - Ayrıca, becerilerin seviyelerini maksimuma çıkarabilirsiniz.
- Oyun oynama esnasında tuş atamalarını değiştirirken kritik bir hata düzeltildi.
- Atlarken veya öfkeli sıçrayış becerisini kullanırken kameranın oyuncuyu takip
etmeme sorunu düzeltildi.
- Öfkeli sıçrayış becerisini kullanırken oyuncunun topa vurma doğruluğu artırıldı.
- Oyuncu atlarsa aynı yerde kalındığı için ceza sıfırlanıyor.
- Aynı anda Nesne haritasının açılmasına ve oyunun duraklatılmasına izin veren,
garip ve istenmeyen davranışlara yol açan sorun düzeltildi.
- Nesne yok etme hesaplamasındaki hata düzeltildi. Sonuç olarak daha az puan
veriliyor.
- Başarısız bir girişimden sonra beceri bekleme süresinin yanlış ayarlanması
sorunu düzeltildi.

## 1.2.4

### Düzeltmeler

- Çeviriler güncellendi ve düzeltildi.

## 1.2.3

### Yeni özellikler

- Yeni çeviriler eklendi.
   - Sırpça. Çevirmen [nidza07](https://github.com/nidza07).
   - Çekçe. Çevirmen [4sensegaming](https://github.com/4sensegaming).

### Düzeltmeler

- Türkçe çeviride küçük bir hata düzeltildi.
- Oyun içi yardımın yanlış görüntülenmesi sorunu düzeltildi.
- Oyun kaydını açarken potansiyel kritik bir hata düzeltildi.

## 1.2.2

Türkçe ve Endonezya dili çevirileri güncellendi.

## 1.2.1

Bu güncelleme, Linux kullanıcıları için birkaç kritik hatayı düzeltiyor.

## 1.2.0

Bu sürüm, kullanıcı deneyimini ve mevcut içeriği daha da iyileştirmeyi
amaçlıyor.  Klavye kısayollarını istediğiniz gibi yeniden atayabilirsiniz.
Oyununuzu kaydedebilir ve bu tür kayıtlar için yerleşik oynatıcıyı kullanarak
kayıtları oynatabilirsiniz. Ayrıca nesne haritası ve diğer bazı iyileştirmeler
ve düzeltmeler de mevcut.

[Github Çeviri Deposu'nu](https://github.com/sooslandia/translations). Kullanıma
sunduk. Oyunu diğer dillere çevirmek istiyorsanız ve yeteneğiniz varsa,
yardımınızı kabul etmekten memnuniyet duyarız.

### Yeni özellikler

- Yeni çeviriler eklendi.
   - Türkçe. Çevirmen [fatihyuksek](https://github.com/fatihyuksek1).
   - Endonezya dili. Çevirmen [MuhammadGagah](https://github.com/MuhammadGagah).
- Varsayılan klavye kısayollarını değiştirebilirsiniz.
   - Bunu yapmak için, ayarlar ekranında, "klavye kısayolu ayarları" sekmesinde
bulunan "klavye kısayollarını özelleştir" düğmesine tıklayın.
   - Ayar dosyanız kullanıcı verileri klasöründe (userData) bulunur ve adı
keyConfig. json'dur. Ayarlarınızı başkalarıyla paylaşabilirsiniz. Başka
birinin ayarlarının sizde çalışması için ayar dosyanızı diğer kişiden aldığınız
dosyayla değiştirmeniz gerekir.
   - Yapılandırma ayarlama hakkında daha fazla bilgiyi kılavuzun ilgili bölümünden
bulabilirsiniz.
- Oyununuzu kayıt altına alabilirsiniz.
   - Oyununuzun kaydedilip kaydedilmeyeceğini belirleyen kutuyu, güncellenmiş oyun
modu seçim ekranından işaretleyebilirsiniz. Kayıt davranışı, Ayarlar ekranının
Kayıt sekmesinden ayarlanabilir.
   - Kayıtları, ana menüden "oyun kayıtları" öğesine erişerek oynatabilirsiniz.
   - Kayıtlar, kullanıcı verileri klasöründe (userData) bulunan recordings klasörüne
kaydedilir ve . sgr uzantısına sahiptir. Kayıt dosyası gerekirse yeniden
adlandırılabilir ve diğer kişilerle paylaşılabilir. Başka birinin kaydının oyun
tarafından algılanabilmesi için oyunun kayıt klasörüne yerleştirilmesi gerekir.
   - Kayıt oynatıcının nasıl çalıştığı ve oynatıcının kısayol tuşları hakkında
bilgi, kılavuzun ilgili bölümünden edinilebilir.
- Nesne haritası eklendi.
   - Oyun esnasında m tuşu ile açılabilir.
   - Haritada yön tuşlarını kullanarak gezinebilirsiniz. Ayrıca, haritada ne kadar
nesne bulunduğunu o tuşuna basarak öğrenebilirsiniz.
   - Haritanın, Kılavuzun nesne haritası bölümünde okuyabileceğiniz iki dolaşım modu
vardır.
   - Tüm nesne haritası kısayol tuşları, klavye kısayolu ayarlarından
değiştirilebilir.
- Ayrıca antrenman modu da genişletilmiştir.
   - Tüm becerilerin bekleme sürelerini f1 tuşuna basarak sıfırlayabilirsiniz.
   - F2 tuşuna bastığınızda, becerilerinizin seviyelerini değiştirebileceğiniz ve
vuruş gücü yenilenme hızını yükseltebileceğiniz bir ekran açılır. Bu ekran
sadece sahip olduğunuz becerileri gösterir. Becerilerinizin seviyesini sadece 1.
seviyeden mevcut maksimum seviyeye değiştirebilirsiniz.
- Ayarlarda, davranış sekmesinde, birinci şahıs görünümünün oyun oturumları
arasında kaydedilip kaydedilmeyeceğini ayarlayabileceğiniz bir onay kutusu
eklendi.
- Kayıtlı oyun ilerlemesi silinebilir ve ayarlar varsayılan değerlere
sıfırlanabilir.
   - Bu, ayarlarda, genel sekmesinden yapılabilir.
   - Ayarlara duraklama menüsünden eriştiyseniz, ayarları sıfırlayamaz veya oyun
ilerlemenizi silemezsiniz.

### Değişiklikler

- Oyun modu seçim ekranı değiştirildi.
   - ekran, menü yerine bir sanal form ile gösteriliyor. Dolaşım, ayarlar veya
profil ekranlarına benziyor.
   - Yeni ekrandan oyununuzun kaydedilip kaydedilmeyeceğini ayarlayabilirsiniz.
- Profil ekranı arayüzü iyileştirildi.
   - İstatistik ekranındaki herhangi bir öğe ctrl+c tuşuna basılarak
kopyalanabiliyor.
   - İstatistik ekranı mevcut başarı puanlarınızı gösteriyor.
   - Auralar ayrıca bonuslarını da görüntülüyor.
- Oyun dengesinde hafif değişiklikler yapıldı.
   - Bin puana kadar her yüz puan için bir para verilecek. Örneğin 678 puan
kazandınız, bu durumda daha önce olduğu gibi bir para değil, yedi para
alacaksınız.
   - Bin puandan sonra her şey eskisi gibi devam eder, ancak alınan on para size
kalır. Örneğin 1234 puan kazandıysanız bu durumda 11 para alırsınız.
- Sahadaki maksimum nesne sayısı artırıldı.
- Birinci şahıs kamera modunda c tuşuna basıldığında çalan ses sahanın ortasından
çalınacak.
- Kritik hata verisi olan dosya adı error yyyy_MM_dd hh-mm-ss.log) olarak
değiştirildi.

### Düzeltmeler

- , kritik hatalar görüntülendiğinde ses döngüye alınmak yerine tamamen
susturulacak.
- Bazı durumlarda oyun kararlılığı iyileştirildi.

## 1.1.1

### Düzeltmeler

- Birinci şahıs modu ve top izleme modu aynı anda etkinken ortaya çıkan kritik
bir hata düzeltildi.
- Diğer küçük hatalar düzeltildi.

## 1.1.0

Bu sürüm, kullanıcı deneyimini iyileştirme odaklıdır: Başarılı sopa vuruş sesi,
birinci şahıs kamera görünümü, alternatif sopa savurma tuşları vs.

### Yeni özellikler

- Oyun  bir veya daha fazla dizesi eksik olan çevirileri destekliyor. Bir dize
bulunamazsa oyun İngilizce dizelere geri dönüyor.
- Top izleme modunda tavana bir arka plan sesi eklendi, bu da izlemeyi daha göz
alıcı hale getirmeye yardımcı olacak.
- Sopa, topa başarılı bir şekilde vurduğunda çalınacak bir ses eklendi.
Varsayılan olarak bildirim devre dışıdır; ayarlardaki "Davranış" sekmesinden
etkinleştirilebilir.
- Birinci şahıs kamera modu eklendi. Modlar arasında geçiş yapmak için, oynarken
v tuşuna basın.
- Güncelleme sırasında oluşan hatalar  userData/errorLogs klasöründe bulunan bir
dosyaya yazılacak.
- Sopayı dikey veya yatay şekilde savurmak için alternatif tuşlar eklendi.
   - Dikey savurma için r, yatay savurma için ise e tuşunu kullanabilirsiniz.
   - Bu çözüm geçicidir ve tuş ayarları uygulanana kadar geçerli olacaktır.
- İstatistik listesinde, ödül mevcut olan öğeler listenin en başında yer alacak.

### Değişiklikler

- Mükemmel vuruş serileri, top tavandan sekme ve topun nesneye çarpması serileri
için puan artırıldı.
- Yeni değişiklikleri göz önüne almak amacıyla kılavuz güncellendi.

### Düzeltmeler

- Sıçramadan sonra iniş sesinin ses seviyesi artırıldı.
- Lider aurası cezalar için puanları arttırmıyor.

## 1.0.0

İlk sürüm.
