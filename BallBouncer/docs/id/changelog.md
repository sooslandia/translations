% log perubahan

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
