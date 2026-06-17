\begin{longtable}{|p{2cm}|p{1.5cm}|p{4cm}|p{3cm}|p{4.5cm}|p{3cm}|p{3.5cm}|}
\caption{Rancangan Pengujian Sistem Food AI Rescue}
\label{tab:rancangan-pengujian} \\
\hline
\rowcolor{gray!25}
\centering\textbf{Fungsio\-nalitas} & \centering\textbf{ID \textit{Test Case}} & \centering\textbf{Deskripsi/Skenario} & \centering\textbf{Pra Kondisi} & \centering\textbf{Langkah Pengujian} & \centering\textbf{Data Pengujian} & \centering\arraybackslash\textbf{Hasil yang Diharapkan} \\ \hline
\endfirsthead

\hline
\rowcolor{gray!25}
\centering\textbf{Fungsio\-nalitas} & \centering\textbf{ID \textit{Test Case}} & \centering\textbf{Deskripsi/Skenario} & \centering\textbf{Pra Kondisi} & \centering\textbf{Langkah Pengujian} & \centering\textbf{Data Pengujian} & \centering\arraybackslash\textbf{Hasil yang Diharapkan} \\ \hline
\endhead

\hline
\endfoot

\hline
\endlastfoot

% 1. Registrasi
\multirow{3}{2cm}{1. Registrasi} 
& TC1.1 & Pengguna mendaftar dengan data valid & Halaman utama pendaftaran & 1. Klik Daftar Gratis \newline 2. Pilih Peran \newline 3. Isi data lengkap \newline 4. Masukkan OTP & $\bullet$ Nama, email, password valid \newline $\bullet$ OTP sesuai & Registrasi berhasil, masuk ke dashboard \\ \cline{2-7}
& TC1.2 & Pengguna mendaftar dengan email yang sudah digunakan & Halaman utama pendaftaran & 1. Isi email yang terdaftar \newline 2. Klik Daftar & $\bullet$ Email sudah terdaftar & Registrasi gagal, pesan error email digunakan \\ \cline{2-7}
& TC1.3 & Pengguna mendaftar dengan konfirmasi password salah & Halaman utama pendaftaran & 1. Isi form \newline 2. Isi konfirmasi password berbeda & $\bullet$ Konfirmasi pass $\neq$ pass & Registrasi gagal, pesan error password salah \\ \hline

% 2. Login
\multirow{2}{2cm}{2. Login} 
& TC2.1 & Pengguna login dengan kredensial valid & Halaman Login & 1. Masukkan email \newline 2. Masukkan password \newline 3. Klik Masuk & $\bullet$ Email = valid \newline $\bullet$ Pass = valid & Login berhasil, diarahkan ke dashboard \\ \cline{2-7}
& TC2.2 & Pengguna login dengan password salah & Halaman Login & 1. Masukkan email \newline 2. Masukkan password \newline 3. Klik Masuk & $\bullet$ Email = valid \newline $\bullet$ Pass = salah & Login gagal, pesan error kredensial salah \\ \hline

% 3. Input Donasi
\multirow{3}{2cm}{3. Input Donasi} 
& TC3.1 & Donatur menambah donasi dengan data valid & Dashboard Donatur (Stok) & 1. Klik Tambah Donasi \newline 2. Isi kelengkapan \newline 3. Unggah foto \newline 4. Publikasikan & $\bullet$ Data valid, kuantitas $>$ 0, foto valid & Donasi berhasil dipublikasikan \\ \cline{2-7}
& TC3.2 & Donatur mengosongkan \textit{field} wajib & Dashboard Donatur (Stok) & 1. Kosongkan nama donasi \newline 2. Klik Publikasikan & $\bullet$ Nama = null & Publikasi gagal, peringatan field wajib \\ \cline{2-7}
& TC3.3 & Donatur memasukkan kuantitas donasi tidak valid & Dashboard Donatur (Stok) & 1. Isi kuantitas nol \newline 2. Klik Publikasikan & $\bullet$ Kuantitas = 0 & Publikasi gagal, peringatan kuantitas \\ \hline

% 4. Claim Donasi
4. Claim Donasi & TC4.1 & Penerima mengklaim donasi yang tersedia & Dashboard Penerima & 1. Pilih donasi \newline 2. Klik Klaim Sekarang \newline 3. Ya, Yakin & $\bullet$ Stok donasi $>$ 0 & Klaim berhasil, tiket klaim dibuat \\ \hline

% 5. Terima Request
\multirow{2}{2cm}{5. Terima Request} 
& TC5.1 & Donatur menyetujui \textit{request} klaim & Dashboard Donatur (Pesanan) & 1. Detail Pesanan \newline 2. Klik Setujui & $\bullet$ Ada pesanan aktif & Request disetujui, pesanan diproses \\ \cline{2-7}
& TC5.2 & Donatur menolak \textit{request} klaim & Dashboard Donatur (Pesanan) & 1. Detail Pesanan \newline 2. Klik Tolak & $\bullet$ Alasan = stok rusak & Request ditolak, pesanan dibatalkan \\ \hline

% 6. Ambil Misi
\multirow{2}{2cm}{6. Ambil Misi} 
& TC6.1 & Relawan mengambil misi pengantaran & Dashboard Relawan & 1. Detail Misi \newline 2. Ambil Misi Ini & $\bullet$ Misi status tersedia & Misi berhasil diambil relawan \\ \cline{2-7}
& TC6.3 & Relawan membatalkan misi yang diambil & Dashboard Relawan & 1. Buka misi aktif \newline 2. Batalkan Misi & $\bullet$ Misi belum diproses & Misi berhasil dibatalkan \\ \hline

% 7. Menunjukkan QR
7. Tunjuk QR & TC7.1 & Relawan menampilkan QR ke donatur & Dashboard Relawan & 1. Buka misi aktif \newline 2. Klik QR Ambil & $\bullet$ Relawan di tahap ambil & QR berhasil ditampilkan \\ \hline

% 8. Scan QR
\multirow{2}{2cm}{8. Scan QR} 
& TC8.1 & Donatur verifikasi resi manual relawan dengan benar & Dashboard Donatur & 1. Verifikasi Manual \newline 2. Input resi \newline 3. Verifikasi & $\bullet$ Kode = PICKUP-9800 & Verifikasi berhasil, makanan diserahkan \\ \cline{2-7}
& TC8.3 & Donatur memasukkan resi manual yang salah & Dashboard Donatur & 1. Verifikasi Manual \newline 2. Input resi \newline 3. Verifikasi & $\bullet$ Kode = PICKUP-0000 & Verifikasi gagal, muncul peringatan \\ \hline

% 9. Verifikasi
\multirow{2}{2cm}{9. Verifikasi Penerima} 
& TC9.1 & Relawan memasukkan kode penerima yang benar & Dashboard Relawan & 1. Buka Scan QR Penerima \newline 2. Input kode \newline 3. Verifikasi & $\bullet$ Kode = FAR-5089 & Verifikasi berhasil, misi selesai \\ \cline{2-7}
& TC9.2 & Relawan memasukkan kode penerima yang salah & Dashboard Relawan & 1. Buka Scan QR Penerima \newline 2. Input kode \newline 3. Verifikasi & $\bullet$ Kode = FAR-0000 & Verifikasi gagal, peringatan kode salah \\ \hline

% % 10. Generate CSR
% 10. CSR & TC10.1 & Donatur meng-\textit{generate} laporan CSR & Dashboard Donatur & 1. Buka menu Kitchen AI \newline 2. Klik Generate CSR & $\bullet$ Riwayat donasi $>$ 0 & CSR berhasil digenerate dalam PDF \\ \hline

% % 11. Generate Resep
% \multirow{2}{2cm}{11. Generate Resep} 
% & TC11.1 & Pengguna meng-\textit{generate} resep makanan via AI & Kitchen AI & 1. Eksplor Kitchen AI \newline 2. Unggah galeri \newline 3. Analisis Bahan & $\bullet$ File foto = valid (.jpg) & Resep AI berhasil ditampilkan \\ \cline{2-7}
% & TC11.2 & Pengguna mencoba \textit{generate} tanpa foto & Kitchen AI & 1. Eksplor Kitchen AI \newline 2. Unggah file non-gambar \newline 3. Analisis Bahan & $\bullet$ File = .md (salah) & Generate gagal, peringatan error upload \\ \hline

\end{longtable}
\end{landscape}