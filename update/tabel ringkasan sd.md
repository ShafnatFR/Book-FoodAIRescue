Daftar dan Spesifikasi *Sequence Diagram*

| No | Peran (*Role*) | Nama *Sequence Diagram* | Spesifikasi Pembahasan (Alur Logika) |
| --- | --- | --- | --- |
| **A** | **Global / Umum** | 1. SD Melakukan *Login* | Menggambarkan alur validasi input kredensial pengguna, pencocokan data di basis data, hingga penerbitan token sesi (JWT) dan pengarahan ke *dashboard* masing-masing peran. |
| **B** | **Penerima** | 2. SD Pencarian & Klaim Makanan | Membahas proses penelusuran katalog makanan, pemilihan metode pengambilan (mandiri/kurir), pembuatan kode unik, hingga pemotongan stok pada basis data. |
|  | (3 Diagram) | 3. SD Pemberian Ulasan (*Review*) | Menggambarkan alur pengiriman penilaian (bintang) dan media foto terhadap makanan/donatur setelah transaksi berstatus selesai (*completed*). |
|  |  | 4. SD Pelaporan Masalah (*Report*) | Membahas proses pengiriman detail komplain (beserta bukti foto) yang akan mengubah status transaksi dan memicu notifikasi peringatan ke dasbor Admin. |
| **C** | **Relawan** | 5. SD Penerimaan Misi Pengantaran | Menggambarkan alur pengambilan penugasan logistik dari *Missions Board*, dilengkapi dengan **blok alternatif penanganan kegagalan (*race condition*)** jika misi ternyata sudah diklaim oleh relawan lain di waktu yang bersamaan. |
|  | (3 Diagram) | 6. SD Validasi Serah Terima (*QR Code* / Manual) | Membahas komunikasi serah terima di mana relawan dapat memindai *QR Code* melalui kamera, atau **memasukkan 6-digit kode unik secara manual** sebagai cadangan (*fallback*) jika perangkat kamera bermasalah. |
|  |  | 7. SD Kalkulasi Gamifikasi (*Sistem Internal*) | Menggambarkan proses sistem berjalan di belakang layar untuk menghitung poin dampak, menaikkan metrik *Experience Point* (XP), dan memperbarui peringkat relawan secara otomatis setelah misi selesai. |
| **D** | **Donatur (Individu)** | 8. SD Unggah Surplus Makanan & Verifikasi AI | Membahas alur formulir bertahap (*multi-step form*) di mana donatur menginput data dan foto makanan, yang kemudian **divalidasi secara langsung oleh AI** (skor keamanan & alergen) sebelum data disimpan dan dipublikasikan ke katalog. |
|  | (3 Diagram) | 9. SD Konfirmasi Pesanan | Membahas proses Donatur saat menerima notifikasi klaim dari Penerima dan melakukan pembaruan status persetujuan (*Approved/Ready*) pada transaksi. |
|  |  | 10. SD Dasbor Dampak Sosial (SROI) | Menggambarkan alur sistem saat menarik agregasi data log transaksi dan mengonversinya menjadi grafik visual reduksi emisi karbon (CO²) dan penghematan air tanah. |
| **E** | **Donatur Korporat** | 11. SD *Generate CSR Copywriter* | *(Spesifik Korporat)* Membahas penarikan data transaksi aktual untuk diolah AI menjadi **dua versi teks (untuk Donatur dan Penerima)** dengan kustomisasi nada dan platform target, disertai fitur pengiriman *request posting* ke akun Penerima. |
|  | (2 Diagram) | 12. SD Pembuatan Logo & Rekomendasi Kemasan | *(Spesifik Korporat)* Menggambarkan alur pemrosesan AI ganda, di mana sistem menghasilkan gambar logo kemasan, sekaligus **menganalisis spesifikasi makanan untuk memberikan rekomendasi material** kemasan (misal: anti-air) dan nama vendor di internet. |
| **F** | **Admin** | 13. SD Verifikasi & Kelola Akun | Menggambarkan alur Admin saat menarik daftar pendaftar baru, memeriksa dokumen identitas, dan mengubah status akun menjadi aktif (terverifikasi) atau ditolak. |
|  | (2 Diagram) | 14. SD Moderasi Komplain | Membahas alur resolusi sengketa, di mana Admin meninjau bukti dari Penerima/Relawan dan menetapkan keputusan status final pada log transaksi (basis data). |
| **G** | **Super Admin** | 15. SD Manajemen Status *Server* | Membahas alur pengaktifan *Maintenance Mode*, yang memicu pemutusan sesi (akses) publik dan mengalihkan seluruh lalu lintas pengguna ke halaman pemeliharaan. |
|  | (1 Diagram) |  |  |
| **Total** | **6 Peran** | **15 *Sequence Diagram*** |  |

---