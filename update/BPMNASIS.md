Berikut adalah penjelasan lengkap mengenai diagram BPMN **As-Is** (sistem saat ini) yang telah dibuat. Penjelasan ini membedah alur kerja, interaksi antaraktor, serta mengidentifikasi kelemahan dari proses yang berjalan secara manual.

### Gambaran Umum
Diagram BPMN As-Is ini memodelkan proses distribusi donasi makanan berlebih yang saat ini masih berjalan secara konvensional. Dalam skenario ini, tidak ada sistem aplikasi cerdas, platform perantara, atau pihak ketiga yang memfasilitasi. Seluruh kegiatan dilakukan murni secara fisik dan manual, yang direpresentasikan menggunakan elemen **Manual Task** (berikon tangan) pada diagram.

### Partisipan (Aktor) yang Terlibat
Proses ini hanya melibatkan dua partisipan utama, yaitu:
1. **Donatur:** Pihak yang memiliki kelebihan makanan dan berinisiatif untuk mendonasikannya.
2. **Penerima:** Pihak yang membutuhkan makanan (seperti panti asuhan, komunitas, atau individu), yang dalam sistem ini bertindak sangat pasif.

---

### Alur Proses (Process Flow)

**1. Pool Donatur (Alur Aktif)**
Donatur adalah penggerak utama dalam sistem konvensional ini. Alurnya adalah sebagai berikut:
*   **Start Event:** Proses dipicu ketika donatur mendapati adanya surplus bahan makanan atau makanan matang yang masih layak konsumsi.
*   **Memiliki bahan/makanan lebih:** Donatur menyortir makanan yang akan didonasikan.
*   **Mengemas makanan:** Donatur membungkus dan mempersiapkan makanan secara mandiri tanpa adanya standar pengemasan tertentu.
*   **Mencari penerima:** Ini adalah fase krusial di mana donatur harus mencari sendiri siapa yang mau menerima makanan tersebut. Biasanya dilakukan dengan bertanya ke tetangga, mencari informasi di internet, atau menyebar pesan di grup obrolan.
*   **Menemukan penerima:** Donatur akhirnya mendapatkan kontak atau lokasi pihak yang bersedia menerima donasi.
*   **Memberikan makanan:** Donatur berangkat menuju lokasi penerima untuk menyerahkan makanan tersebut secara langsung.
*   **End Event:** Proses dari sisi donatur selesai setelah makanan berpindah tangan.

**2. Pool Penerima (Alur Pasif)**
*   **Start Event:** Penerima pada dasarnya hanya dalam posisi menunggu adanya pihak yang menawarkan bantuan.
*   **Makanan diterima:** Aktivitas tunggal di mana penerima melakukan serah terima donasi secara fisik dari donatur.
*   **End Event:** Siklus dari sisi penerima selesai.

**3. Pertukaran Pesan (Message Flow)**
Terdapat garis putus-putus (*Message Flow*) yang menghubungkan aktivitas **"Memberikan makanan"** (di *pool* Donatur) dengan aktivitas **"Makanan diterima"** (di *pool* Penerima). Garis ini merepresentasikan interaksi fisik di dunia nyata, yaitu perpindahan kotak makanan dari tangan donatur ke tangan penerima.

---

### Analisis Kelemahan Sistem As-Is (Pain Points)

Dari alur yang tergambar, BPMN ini secara eksplisit memperlihatkan mengapa sistem yang ada saat ini tidak efisien dan membutuhkan perbaikan (sistem *To-Be*). Berikut adalah hambatannya:

*   **Titik Buta Informasi (Inefisiensi Waktu):** Aktivitas "Mencari penerima" memakan waktu yang sangat lama. Tidak ada *database* atau *matchmaking* yang menghubungkan donatur dengan pihak yang benar-benar membutuhkan secara *real-time*.
*   **Risiko Logistik (Ketiadaan Relawan/Kurir):** Karena tidak ada pihak ketiga, aktivitas "Memberikan makanan" membebani donatur. Jika donatur sibuk atau tidak punya kendaraan, donasi bisa tertunda. Akibatnya, ada risiko makanan membusuk sebelum sempat didonasikan.
*   **Isu Keamanan Pangan (Food Safety):** Karena semua berjalan tertutup antara dua pihak, tidak ada verifikasi eksternal saat tahap "Mengemas makanan". Penerima tidak memiliki jaminan pasti mengenai tingkat higienitas makanan tersebut selain rasa percaya kepada donatur.