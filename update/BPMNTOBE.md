Berikut adalah penjelasan lengkap mengenai diagram BPMN **To-Be** (sistem usulan/harapan) yang menggambarkan alur proses setelah didigitalisasi menggunakan aplikasi.

### Gambaran Umum
Sistem To-Be merombak total cara kerja konvensional menjadi terpusat pada sebuah aplikasi digital[cite: 2]. Proses tidak lagi mengandalkan komunikasi manual (seperti *chat* atau mencari dari pintu ke pintu), melainkan diotomatisasi melalui platform yang menghubungkan berbagai pihak secara *real-time*[cite: 2].

### Partisipan (Aktor) yang Terlibat
Pada sistem yang baru ini, terdapat penambahan satu aktor penting yang difasilitasi oleh sistem[cite: 2]:
1. **Penerima:** Pengguna aplikasi yang mencari dan memesan donasi makanan[cite: 2].
2. **Donatur:** Pihak yang memposting ketersediaan makanan berlebih untuk didonasikan[cite: 2].
3. **Relawan (Aktor Baru):** Pihak ketiga yang bertugas sebagai pahlawan logistik (kurir) untuk menjembatani donatur dan penerima[cite: 2].

---

### Alur Proses Utama (Process Flow)

**1. Pool Penerima (Pusat Kendali Pemesanan)**
Penerima kini menjadi pihak yang aktif memilih donasi[cite: 2]. Alurnya adalah:
* **Autentikasi:** Penerima membuka aplikasi dan diwajibkan untuk *Login* atau *Register* jika belum memiliki akun[cite: 2].
* **Eksplorasi & Order:** Masuk ke halaman beranda, mencari makanan yang diinginkan, dan melakukan order jika menemukannya[cite: 2].
* **Opsi Logistik:** Sistem mengecek ketersediaan alamat[cite: 2]. Setelah itu, penerima dihadapkan pada *Gateway* percabangan metode pengambilan[cite: 2]:
  * **Pick up:** Penerima datang langsung ke lokasi donatur[cite: 2].
  * **Diantar:** Sistem secara otomatis akan mem- *broadcast* pesanan tersebut menjadi "misi" bagi para relawan[cite: 2].

**2. Pool Donatur (Penyedia Donasi)**
Alur donatur menjadi jauh lebih ringkas dan terarah[cite: 2]:
* **Notifikasi:** Donatur menerima notifikasi order dari sistem, lalu mulai mengemas makanan[cite: 2].
* **Menunggu & Validasi:** Donatur cukup menunggu pihak pengambil (Penerima atau Relawan) datang[cite: 2]. 
* **Keamanan (QR Code):** Saat pengambil tiba, donatur akan meminta QR Code atau kode unik, melakukan *scan* via aplikasi, dan baru menyerahkan makanan setelah data valid[cite: 2].

**3. Pool Relawan (Penyelesai Kendala Logistik)**
Alur ini hanya terpicu jika penerima memilih metode "Diantar"[cite: 2]:
* **Klaim Misi:** Relawan menerima notifikasi misi logistik di sekitarnya dan melakukan "Klaim misi"[cite: 2].
* **Pengambilan:** Relawan menuju lokasi donatur, melewati proses verifikasi QR dari donatur, dan menerima makanan[cite: 2].
* **Pengantaran:** Relawan mengantarkan makanan ke lokasi penerima[cite: 2].
* **Validasi Akhir:** Di lokasi tujuan, relawan meminta QR Code dari penerima, melakukan *scan*, dan menyerahkan makanan[cite: 2].

---

### Solusi yang Ditawarkan (Perbaikan dari Sistem As-Is)

Sistem To-Be ini secara langsung menyelesaikan kelemahan-kelemahan ( *pain points* ) pada sistem As-Is:
* **Mengatasi *Blind Spot* Informasi:** Fitur aplikasi membuat donatur tidak perlu pusing mencari siapa yang mau menerima donasi. Penerima dapat langsung melihat ketersediaan makanan di beranda aplikasi dan memesannya seketika[cite: 2].
* **Menyelesaikan Kendala Logistik:** Kehadiran entitas **Relawan** memastikan rantai pasok tidak terputus[cite: 2]. Jika donatur tidak bisa mengantar dan penerima tidak bisa mengambil, relawan akan mengambil alih misi tersebut[cite: 2].
* **Validasi & Keamanan Pangan (Fitur QR Code):** Proses *Scan* QR Code yang dilakukan oleh Donatur dan Relawan memastikan bahwa donasi jatuh ke tangan orang yang tepat secara sistem[cite: 2]. Ini juga meminimalisir penipuan dan memberikan *tracking* yang jelas kapan makanan dipindah tangankan[cite: 2].