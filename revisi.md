Berdasarkan analisis pada dokumen buku/tugas akhir Anda (`main.pdf`), secara keseluruhan penulisan Bab 3 Anda sudah sangat terstruktur. Namun, ada beberapa subbab yang langsung melompat ke poin-poin atau diagram tanpa adanya "paragraf pengantar" (jembatan paragraf). Dalam penulisan akademis, setiap kali ada judul bab atau subbab baru, wajib diberikan minimal 1-2 paragraf pembuka sebelum masuk ke sub-subbab di bawahnya.

Berikut adalah analisis dan saran teks pembuka (*introductory paragraphs*) yang jauh lebih akademis, mengalir, dan komprehensif untuk menyempurnakan Bab 3 Anda:

### 1. Di Bawah Judul Utama "BAB III PEMODELAN DAN PERANCANGAN"

**Analisis:** Saat ini, setelah judul "BAB III PEMODELAN DAN PERANCANGAN", teks langsung melompat ke subbab "3.1 Arsitektur Sistem". Hal ini membuat bab terasa terputus.
**Saran Teks Pembuka (Tambahkan sebelum 3.1):**

> "Bab ini menguraikan secara komprehensif tahapan pemodelan dan perancangan platform *Food AI Rescue* (FAR). Pembahasan difokuskan pada rancang bangun arsitektur sistem yang mengintegrasikan teknologi *Progressive Web App* (PWA) dengan antarmuka Kecerdasan Buatan (AI). Selain itu, bab ini juga memetakan desain logika sistem dan struktur basis data relasional, perancangan antarmuka pengguna berbasis *Human-Centered Design*, serta merincikan spesifikasi infrastruktur teknologi yang dibutuhkan untuk mendukung fase pengembangan hingga implementasi produksi platform."

---

### 2. Subbab 3.1 Arsitektur Sistem

**Analisis:** Teks saat ini sudah cukup baik dalam menjelaskan PWA dan Multi-Tier Architecture. Namun, bahasanya bisa dipertajam agar lebih menonjolkan alasan pemilihan arsitektur tersebut terkait performa.
**Saran Teks Pembuka:**

> "Arsitektur sistem merupakan fondasi struktural yang menentukan bagaimana setiap komponen di dalam platform *Food AI Rescue* saling berinteraksi, memproses data, dan memberikan respons kepada pengguna. Guna memastikan kinerja operasional yang skalabel, aman, dan responsif secara *real-time*, sistem ini dirancang dengan mengadopsi pendekatan *Multi-Tier Architecture* berbasis *client-server*. Ekosistem perangkat lunak ini diwujudkan dalam bentuk *Progressive Web App* (PWA) yang terbagi menjadi tiga lapisan komputasi utama, yaitu lapisan presentasi (*frontend*), lapisan logika bisnis (*backend*), dan lapisan data (*database*)."

---

### 3. Subbab 3.2 Pemodelan Sistem dan Data

**Analisis:** Di dokumen Anda, setelah judul 3.2, teks langsung melompat ke "3.2.1 Use Case Diagram" tanpa ada kalimat pengantar.
**Saran Teks Pembuka (Tambahkan sebelum 3.2.1):**

> "Tahapan pemodelan sistem dan data bertujuan untuk memvisualisasikan alur interaksi aktor, struktur logika bisnis, dan organisasi penyimpanan informasi di dalam platform *Food AI Rescue*. Rancang bangun ini direpresentasikan melalui serangkaian diagram analitis standar *Unified Modeling Language* (UML) dan pemodelan relasional, yang meliputi *Use Case Diagram* untuk memetakan batasan fungsional aktor, *Entity Relationship Diagram* (ERD) untuk arsitektur pangkalan data, *Class Diagram* untuk memetakan struktur objek pada peladen (*server*), serta *Sequence Diagram* untuk memvisualisasikan skenario pertukaran pesan dinamis pada fitur-fitur krusial."

---

### 4. Subbab 3.3 Perancangan Antarmuka Pengguna

**Analisis:** Paragraf Anda saat ini sudah bagus karena menyebutkan *Human-Centered Design* dan artefak UX. Namun, bisa diperkaya dengan rincian apa saja yang akan dibahas di dalam subbab ini (prinsip, halaman, navigasi).
**Saran Teks Pembuka:**

> "Perancangan antarmuka pengguna (*User Interface*/UI) pada platform *Food AI Rescue* dikembangkan dengan berlandaskan pada prinsip *Human-Centered Design* (HCD). Mengacu pada hasil ekstraksi artefak *User Experience* (UX) pada tahap analisis—seperti *User Persona*, *Empathy Map*, dan *Customer Journey Map*—desain visual dirancang secara spesifik untuk memecahkan titik keluhan (*pain points*) pengguna di lapangan. Subbab ini akan menjabarkan prinsip desain visual antarmuka, tata letak fungsional untuk masing-masing peran dalam ekosistem *Role-Based Access Control* (RBAC), serta pemetaan alur navigasi kritis guna memastikan pengalaman pengguna yang intuitif, inklusif, dan responsif lintas perangkat."

---

### 5. Subbab 3.4 Kebutuhan Perangkat Keras dan Perangkat Lunak

**Analisis:** Sama seperti 3.2, judul ini langsung melompat ke sub-subbab 3.4.1 tanpa ada penjelasan pengantar.
**Saran Teks Pembuka (Tambahkan sebelum 3.4.1):**

> "Guna menunjang keberhasilan rancang bangun platform *Food AI Rescue*—baik pada fase rekayasa lokal maupun penerapan di tingkat produksi (*deployment*)—diperlukan spesifikasi infrastruktur teknologi yang terukur dan andal. Subbab ini merincikan daftar kebutuhan spesifikasi minimum perangkat keras (*hardware*) dan perangkat lunak (*software*) yang berfungsi sebagai lingkungan operasional (*environment*) bagi sistem basis data, peladen *backend*, integrasi API *Machine Learning*, hingga perangkat akses akhir yang digunakan oleh pengguna di lapangan."