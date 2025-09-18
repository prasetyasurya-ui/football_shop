⚽ Wolverhampton Shop - Proyek Django

Selamat datang di repositori Wolverhampton Shop, sebuah aplikasi web e-commerce sederhana yang dibangun menggunakan framework Django. Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Pengembangan Berbasis Platform (PBP).

## Tugas Individu 4

**[🔗 Kunjungi Aplikasi yang Sudah Deploy](https://prasetya-surya-footballshop.pbp.cs.ui.ac.id/)**

**[🔗 Tugas Individu 3](https://github.com/prasetyasurya-ui/football_shop/wiki/Tugas-Individu-3)**

# Langkah-Langkah Implementasi

##  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.

Pengimplementasian fungsi registrasi adalah dengan menggunakan UserCreationForm dari Django dan	apabila input yang diberikan valid maka User akan terbuat dan disimpan ke dalam basis data.

Pengimplementasian fungsi login adalah dengan menggunakan AuthenticationForm dari Django dan apabila kredensial yang diberikan valid maka User akan diambil dari basis data dan login dengan fungsi login dari Django.

Pengimplementasian fungsi logout adalah dengan menggunakan fungsi logout dari Django

## Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
Dengan registrasi akun baru dan add product
Akun Pertama: pabubu
password: pokpokpok
Produk: Baju Champions, Baju Masters, Baju CN

Akun Kedua: bububu
password: pakpakpak
Produk: Celana Jeans, Celana Chino, Celana beige

## Menghubungkan model Product dengan User.
Karena Product dan user memiliki hubungan Many-to-One maka kita akan menambahkan field user/owner pada Model Product menggunakan code
```python
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
```

##  Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
Untuk menampilkan informasi username dan last login, menambahkan HTML untuk menampilkan username dan last_login.

Untuk penerapan cookies seperti last_login. Menggunakan code di Bawah ini di fungsi `login_user` Ketika berhasil login	
```python
response.set_cookie('last_login', str(datetime.datetime.now()))
```

##  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm adalah kelas form bawaan Django yang dirancang khusus untuk otentikasi pengguna. AuthenticationForm akan memverifikasi kredensial yang dimasukkan oleh seeseorang cocok dengan yang ada di basis data

### Kelebihan
- Memudahkan dalam membuat form untuk login, otomatis membuat form dengan field username, password
- Aman karena memiliki proteksi terhadap CSRF
- Validasi otomatis

### Kekurangan
- Kustomisasi manual, missal ingin menambahkan email sebagai gantinya username, harus membuat subclass AuthenticationForm

---

## Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses memverifikasi siapa orang yang ingin login
Otorisasi adalah proses pemberian izin ke orang yang sudah terautentikasi sesuai dengan hak aksesnya

Django mengimplementasikan autentikasi dengan pengecekan kredensial terhadap basis data
Django mengimplementasikan otorisasi dengan otomatis membuat izin `add`, `change`, `delete`, dan `view` untuk setiap Model yang dibuat. Django bisa memberi izin kepada pengguna secara individu atau mengelompokkannya ke dalam Groups untuk pengelolaan yang lebih mudah

##  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web? 

### Kelebihan Session
- Kapasitas penyimpanan 5MB
- Bisa menyimpan tipe data kompleks

### Kekurangan Session
- Data hilang Ketika tab/window ditutup
- Tidak cocok untuk data persistent

### Kelebihan Cookies
- Persistent Data Storage

### Kekurangan Cookies
- Kapasitas hanya 4KB
- Kurang aman

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Cookies tidak aman secara default. Risiko potensial cookies yang harus diwaspadai adalah Cross-Site Scripting (XSS), yaitu jika penyerang menyuntikkan skrip jahat ke halaman web dan mencuri cookie yang berisi informasi. Hal lain yang harus diwaspadai adalah Cross-Site Request Forgery (CSRF), yaitu User yang sedang login di suatu web mengunjungi situs jahat yang akan mengirimkan form atau link ke web tersebut dengan aksi jahat (misalnya, transfer bank dan ubah password) dan server web tersebut menganggap request tersebut valid karena cookie autentikasi dikirim bersamaan form

Django mengamankan Cookies dengan `CSRF_TOKEN`. Untuk setiap permintaan `POST` Django mewajibkan adanya "token CSRF". Token ini adalah sebuah string acak yang disimpan di cookie dan juga disisipkan sebagai hidden input di form HTML. Saat form disubmit, Django akan memverifikasi apakah token di cookie sama dengan token di form.