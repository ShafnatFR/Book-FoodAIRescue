Berikut adalah tabel penjelasan rincian *Class Diagram* yang telah disusun secara terstruktur sesuai dengan format kolom yang Anda minta. Tabel ini siap untuk Anda salin langsung ke dalam dokumen draf Buku Tugas Akhir Anda.

**Tabel 3.X** Penjelasan Rincian *Class Diagram* Food AI Rescue (FAR)

| No | Nama Kelas & Stereotype | Deskripsi / Fungsi | Atribut Utama | Operasi / Metode Utama |
| --- | --- | --- | --- | --- |
| 1 | **System Enums**<br>

<br>`<<enumeration>>` | Kumpulan tipe data statis konstan yang digunakan untuk membatasi nilai input (seperti jenis peran, status makanan, dan metode pengiriman) guna mencegah anomali data di seluruh sistem. | `UserRole`, `FoodStatus`, `ClaimStatus`, `DeliveryMethod` | *(Tidak memiliki operasi/metode, hanya berisi nilai konstan)* |
| 2 | **UserData**<br>

<br>`<<entity>>` | Merepresentasikan model data profil pengguna terdaftar, termasuk penyimpanan kredensial, peran (*role*), dan total poin kontribusi (SROI/XP). | `id`, `name`, `email`, `role`, `status`, `points`, `phone`, `address`, `password` | `authenticate()`, `updatePoints()`, `verifyOTP()` |
| 3 | **FoodItem**<br>

<br>`<<entity>>` | Merepresentasikan model data inventaris makanan surplus dari donatur. Menyimpan data kuantitas, waktu kadaluarsa, hingga hasil JSON verifikasi AI dan kalkulasi dampak sosial. | `id`, `providerId`, `name`, `currentQuantity`, `expiryTime`, `aiVerification`, `socialImpact` | `deductStock()`, `checkExpiry()`, `updateStatus()` |
| 4 | **ClaimHistoryItem**<br>

<br>`<<entity>>` | Merepresentasikan model log transaksi pesanan yang menghubungkan entitas Donatur, Penerima, dan Relawan. Menyimpan kode unik serah terima dan data ulasan. | `id`, `foodId`, `receiverId`, `volunteerId`, `uniqueCode`, `status`, `rating`, `review` | `generateQR()`, `assignVolunteer()`, `scanAndComplete()` |
| 5 | **Address**<br>

<br>`<<entity>>` | Model data yang menyimpan detail koordinat geolokasi dan alamat fisik pengguna untuk keperluan pemetaan dan penjemputan logistik. | `id`, `userId`, `label`, `fullAddress`, `lat`, `lng`, `contactPhone` | *(Sebagai entitas data murni, dimanipulasi oleh layanan basis data)* |
| 6 | **DatabaseService**<br>

<br>`<<service>>` | Modul *backend* utama yang bertugas mengelola koneksi dan mengeksekusi kueri langsung ke basis data MySQL (proses CRUD transaksi). | `API_URL`, `headers` | `registerUser()`, `loginUser()`, `addFoodItem()`, `processClaimTransaction()`, `getClaims()` |
| 7 | **AIService**<br>

<br>`<<service>>` | Layanan integrasi sistem cerdas yang menangani komunikasi (API *Call*) ke model *Google Gemini* untuk validasi makanan dan *Generate* CSR. | `apiKeys`, `currentKeyIndex`, `model` | `verifyFoodSafety()`, `generateCSRContent()`, `designPackaging()`, `rotateKey()` |
| 8 | **FileService**<br>

<br>`<<service>>` | Modul pengelola media untuk menangani kompresi, penyimpanan (*upload*), dan penghapusan berkas gambar/foto ke dalam direktori lokal server. | `uploadPath`, `maxFileSize` | `uploadImage()`, `optimizeImage()`, `deleteFile()` |
| 9 | **GamificationService**<br>

<br>`<<utility>>` | Skrip utilitas (*helper*) yang berisi logika kalkulasi untuk menghitung *Experience Point* (XP), menentukan pangkat (*rank*), dan memberikan lencana ke pengguna. | `rankLevels`, `badges` | `calculateXP()`, `evaluateRank()`, `awardBadge()`, `getLeaderboard()` |
| 10 | **ExpiryChecker**<br>

<br>`<<utility>>` | Pekerja latar belakang (*background job*) yang secara berkala memeriksa waktu dan mengubah status makanan jika telah melewati batas waktu aman konsumsi. | *(Skrip berjalan independen tanpa atribut state tetap)* | `checkAndExpireItems()`, `isFoodExpired()` |
| 11 | **App**<br>

<br>`<<component>>` | Komponen akar (*root*) dari *Frontend* (React) yang bertindak sebagai *router* utama pengelola sesi dan pengarah antarmuka ke dasbor masing-masing *role*. | `currentView`, `role`, `currentUser`, `isDarkMode` | `handleLogin()`, `handleLogout()`, `handleClaimFood()`, `renderContent()` |
| 12 | **ProviderIndex**<br>

<br>`<<component>>` | Komponen antarmuka pengguna untuk Donatur (Individu/Korporat). Mengelola UI inventaris, riwayat donasi, dan pemicu alat AI Korporat. | `foodItems`, `claimHistory` | `renderDashboard()`, `renderInventory()`, `renderOrders()` |
| 13 | **ReceiverIndex**<br>

<br>`<<component>>` | Komponen antarmuka pengguna untuk Penerima. Mengelola UI katalog makanan yang tersedia dan formulir penyelesaian klaim/laporan. | `availableFood`, `selectedFood` | `renderFoodList()`, `renderFoodDetail()`, `handleClaim()` |
| 14 | **VolunteerIndex**<br>

<br>`<<component>>` | Komponen antarmuka pengguna untuk Relawan. Mengelola UI papan misi (*Missions Board*) geografis dan visualisasi *leaderboard* gamifikasi. | `missions`, `leaderboard` | `renderMissions()`, `acceptMission()`, `renderLeaderboard()` |
| 15 | **AdminIndex**<br>

<br>`<<component>>` | Komponen antarmuka pengguna panel kontrol untuk Administrator. Digunakan untuk memoderasi laporan sengketa dan memverifikasi pengguna baru. | `users`, `reports`, `systemLogs` | `renderCommunity()`, `renderModeration()`, `verifyUser()` |