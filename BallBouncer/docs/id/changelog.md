% log perubahan

## 1.3.2

### Perbaikan

- Successful bat hit sound has been fixed and now plays in all intended
situations.
- Information on how to activate items has been added to the descriptions of
trial of will and trial of mastery modes.
- Fixed a game crash that occurred when a screen reader other than NVDA was
active.
- Issues with mp3 recordings have been fixed.
   - Potentially fixed a game crash that occurred when playing with recording
enabled.
   - A special VBR header is now added to recordings. Previously, its absence could
cause some players to incorrectly display the recording's duration and
experience issues with seeking.
   - MP3 encoding parameters have been adjusted to reduce file size without
noticeable quality loss.-
- A line has been added to the documentation explaining how to unlock the quest
board (in the "Other Game Modes" section).
- Fixed a critical error that occurred when many sounds were playing
simultaneously.

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

### Fitur baru

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

### Perubahan

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

### Perbaikan

- Updated and corrected translations.

## 1.2.3

### Fitur baru

- Terjemahan baru ditambahkan.
   - Serbian. Translator [nidza07](https://github.com/nidza07).
   - Czech. Translator [4sensegaming](https://github.com/4sensegaming).

### Perbaikan

- Resolved a minor issue in the Turkish translation.
- Fixed incorrect display of in-game help.
- Fixed a potential critical error when loading a recording.

## 1.2.2

Updated Turkish and Indonesian translations.

## 1.2.1

Pembaruan ini memperbaiki beberapa bug penting bagi pengguna Linux.

## 1.2.0

Versi ini ditujukan untuk lebih meningkatkan pengalaman pengguna dan pemolesan
konten yang ada. Sekarang Anda dapat menetapkan ulang pintasan keyboard sesuai
keinginan. Sekarang Anda dapat merekam permainan Anda dan memutar ulang rekaman
yang dihasilkan menggunakan pemutar bawaan untuk rekaman tersebut. Peta objek
dan beberapa perbaikan dan perbaikan lainnya juga tersedia.

Kami telah membuka [repositori terjemahan github] resmi
(https://github.com/sooslandia/translations). Jika Anda ingin menerjemahkan game
dan memiliki kemampuan, kami akan dengan senang hati menerima bantuan Anda.

### Fitur baru

- Terjemahan baru ditambahkan.
   - Turki. Penerjemah [fatihyuksek](https://github.com/fatihyuksek1).
   - Indonesia. Penerjemah [MuhammadGagah](https://github.com/MuhammadGagah).
- Anda sekarang dapat mengubah pintasan keyboard bawaan.
   - Untuk melakukannya, klik tombol "Sesuaikan Pintasan Keyboard" yang terletak di
tab "Konfigurasi Pintasan Keyboard" pada layar Pengaturan.
   - File konfigurasi Anda terletak di folder data pengguna (userData) dan disebut
keyConfig.json. Anda dapat membagikan konfigurasi Anda dengan orang lain. Agar
konfigurasi orang lain berfungsi untuk Anda, Anda perlu mengganti file
konfigurasi Anda dengan file yang Anda terima dari orang lain.
   - Anda dapat mengetahui lebih lanjut tentang pengaturan konfigurasi di bagian
dokumentasi yang sesuai.
- Anda sekarang dapat merekam gameplay Anda.
   - Anda dapat mencentang kotak yang menentukan apakah sesi permainan Anda akan
direkam pada layar pemilihan mode permainan yang diperbarui. Perilaku
perekaman dapat dikonfigurasi di tab Perekaman pada layar Pengaturan.
   - Anda dapat memutar rekaman dari menu rekaman, yang dapat diakses dengan
mengaktifkan item terkait di menu utama.
   - Rekaman disimpan dalam folder rekaman, terletak di folder data pengguna
(userData) dan berekstensi .sgr. File rekaman dapat diganti namanya jika perlu
dan dibagikan dengan orang lain. Agar rekaman orang lain dapat terdeteksi oleh
game, maka harus ditempatkan di folder rekaman game tersebut.
   - Informasi tentang cara kerja pemutar rekaman dan tombol kontrolnya dapat
ditemukan di bagian dokumentasi terkait.
- Menambahkan peta objek.
   - Itu dapat dibuka dengan tombol m selama sesi permainan.
   - Navigasi peta menggunakan tombol panah. Anda juga dapat mengetahui berapa
banyak objek yang ada di peta dengan menekan tombol o.
   - Ada dua mode navigasi, yang dapat Anda baca di bagian dokumentasi terkait.
   - Semua tombol pintas peta objek dapat diubah dalam konfigurasi pintasan keyboard.
- Mode pelatihan juga diperluas.
   - Anda sekarang dapat langsung menghilangkan cooldown semua skill dengan menekan
f1.
   - Saat Anda menekan tombol f2, sebuah layar akan terbuka di mana Anda dapat
mengubah level keterampilan Anda dan tingkat pemulihan kekuatan pukulan. Layar
ini hanya menampilkan skill yang Anda miliki. Anda dapat mengubah levelnya hanya
dalam rentang dari level 1 hingga level maksimum saat ini.
- Dalam pengaturan, pada tab "Perilaku", sebuah kotak centang telah ditambahkan
yang menentukan apakah status tampilan orang pertama akan dipertahankan di
antara sesi permainan.
- Sekarang dimungkinkan untuk menghapus kemajuan permainan yang disimpan dan
mengatur ulang pengaturan ke nilai default.
   - Ini dapat dilakukan di pengaturan, pada tab "Umum".
   - Anda tidak akan dapat mengatur ulang pengaturan atau menghapus kemajuan Anda
jika Anda mengakses pengaturan melalui menu jeda.

### Perubahan

- Layar pemilihan mode permainan telah diubah.
   - layar sekarang diwakili oleh bentuk virtual, bukan menu. Navigasinya mirip
dengan pengaturan atau layar profil.
   - Dari layar baru Anda dapat menentukan apakah sesi permainan akan direkam.
- Antarmuka layar profil yang ditingkatkan.
   - Sekarang item apa pun dari daftar statistik dapat disalin ke clipboard dengan
menekan ctrl+c.
   - Tab statistik sekarang menampilkan jumlah poin pencapaian saat ini.
   - Aura sekarang juga menampilkan bonusnya.
- Sedikit perubahan pada keseimbangan permainan.
   - Sekarang untuk setiap seratus poin hingga seribu, satu koin akan diberikan.
Misalnya, Anda mencetak 678 poin, dalam hal ini Anda akan menerima 7 koin, dan
bukan satu koin seperti sebelumnya.
   - Setelah seribu poin, semuanya tetap seperti sebelumnya, tetapi 10 koin yang
diterima tetap milik Anda. Misalnya, Anda mencetak 1234 poin, dalam hal ini
Anda akan menerima 11 koin.
- Jumlah maksimum objek di lapangan telah ditingkatkan.
- Sekarang suara yang diputar dengan menekan tombol c dalam mode kamera orang
pertama akan diputar di tengah lapangan.
- Format nama file dengan data kesalahan kritis telah diubah menjadi (kesalahan
yyyy_MM_dd hh-mm-ss.log)

### Perbaikan

- Sekarang, ketika kesalahan kritis ditampilkan, suara akan dibungkam sepenuhnya,
bukan diulang-ulang.
- Peningkatan stabilitas game dalam beberapa kasus.

## 1.1.1

### Perbaikan

- Memperbaiki bug kritis yang terjadi ketika mode orang pertama dan mode menonton
bola aktif secara bersamaan.
- Memperbaiki beberapa bug kecil lainnya.

## 1.1.0

Versi ini difokuskan pada peningkatan pengalaman pengguna: Suara pukulan tongkat
yang berhasil, tampilan kamera orang pertama, tombol ayunan tongkat alternatif,
dll.

### Fitur baru

- Game ini sekarang mendukung terjemahan yang kehilangan satu atau lebih string.
Jika string tidak ditemukan, permainan akan kembali ke string lokalisasi
bahasa Inggris.
- Dalam mode menonton bola, suara latar telah dipasang di langit-langit, yang
akan membantu membuat menonton menjadi lebih spektakuler.
- Menambahkan suara yang menunjukkan kapan tongkat pemukul berhasil mengenai
bola. Secara default, notifikasi dinonaktifkan; Dapat diaktifkan di
pengaturan, pada tab "Perilaku".
- Menerapkan mode kamera orang pertama. Untuk beralih antar mode, tekan v saat
bermain.
- Kesalahan selama pembaruan sekarang ditulis ke file yang akan ditempatkan di
folder userData/errorLogs.
- Menambahkan kunci alternatif untuk membuat ayunan tongkat horizontal dan
vertikal.
   - Untuk ayunan horizontal gunakan tombol e, untuk ayunan vertikal gunakan tombol
r.
   - Solusi ini bersifat sementara dan tetap ada hingga konfigurasi kunci diterapkan.
- Sekarang item dengan hadiah yang tersedia di daftar statistik ada di awal
daftar.

### Perubahan

- Peningkatan poin yang diterima untuk pukulan beruntun yang sempurna, bola
memantul ke langit-langit dan bola dengan pantulan objek beruntun.
- Dokumentasi telah diperbarui untuk mempertimbangkan fitur-fitur baru.

### Perbaikan

- Meningkatkan volume suara pendaratan setelah melompat.
- Kini aura pemimpin tidak menambah poin yang hilang akibat penalti.

## 1.0.0

Rilis pertama.
