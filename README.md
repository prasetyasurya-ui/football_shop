⚽ Football Shop - Proyek Django

Selamat datang di repositori Football Shop, sebuah aplikasi web e-commerce sederhana yang dibangun menggunakan framework Django. Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Pengembangan Berbasis Platform (PBP).

**[🔗 Kunjungi Aplikasi yang Sudah Deploy](https://prasetya-surya-footballshop.pbp.cs.ui.ac.id/)**

## Langkah-Langkah Implementasi

Berikut adalah rincian langkah demi langkah dalam membangun proyek ini dari awal hingga deployment.

### 1. Inisialisasi Proyek dan Lingkungan
Langkah pertama adalah menyiapkan fondasi proyek yang bersih dan terisolasi.
- Membuat direktori dimana projek Django akan dibuat
- Membuat virtual environment agar mengisolasi package dan versi dependencies di komputer tidak bertabrakan
- Mengaktifkan virtual environment menggunakan `env\Scripts\Activate`
- Menyiapkan dependencies dengan mengikuti tutorial 0 dan menginstall dependencies menggunakan pip
- Start projek django football_shop dengan command `django-admin startproject football_shop .`

### 2. Konfigurasi Proyek
- **Environment Variables**: Untuk keamanan, variabel sensitif seperti `SECRET_KEY` dan konfigurasi database tidak ditulis langsung di kode, melainkan dikelola sebagai *environment variable*.
- **Modifikasi `settings.py`**: File `settings.py` disesuaikan untuk membaca *environment variable*, mengonfigurasi koneksi database, dan menambahkan `localhost` serta `127.0.0.1` ke `ALLOWED_HOSTS` untuk pengembangan lokal.
- **Migrasi Awal dan Uji Coba**: Database diinisialisasi dengan `python manage.py migrate` dan server pengembangan lokal dijalankan lewat `python manage.py runserver` untuk memastikan semua konfigurasi berjalan lancar.
- **Version Control**: Proyek diunggah ke GitHub untuk manajemen versi dan kolaborasi.

### 3. Pembuatan Aplikasi `main`
Aplikasi inti bernama `main` dibuat untuk menangani fungsionalitas utama toko.
- **Membuat Aplikasi**: Aplikasi dibuat dengan perintah `python manage.py startapp main`.
- **Registrasi Aplikasi**: Aplikasi `main` kemudian didaftarkan ke dalam proyek dengan menambahkannya ke daftar `INSTALLED_APPS` di `settings.py`.

### 4. Routing dan Model
- **Routing Utama**: Di `football_shop/urls.py`, sebuah rute ditambahkan untuk mengarahkan semua permintaan dari *root URL* (`''`) ke file `urls.py` milik aplikasi `main` menggunakan `include('main.urls')`.
- **Routing Aplikasi**: Di dalam direktori `main`, file `main/urls.py` dibuat untuk memetakan URL ke fungsi-fungsi spesifik yang ada di `main/views.py`.
- **Pembuatan Model `Product`**: Di `main/models.py`, sebuah *class* model bernama `Product` dibuat. Model ini mendefinisikan struktur data untuk setiap produk di database, lengkap dengan atribut-atribut wajib seperti nama, harga, deskripsi, dan ID unik menggunakan `UUID`.

### 5. Deployment
Aplikasi yang sudah selesai dikembangkan kemudian di-deploy agar bisa diakses secara publik.
- **Koneksi ke Git**: Repositori lokal dihubungkan dengan repositori di platform deployment.
- **Deployment ke PWS**: Proses deployment dilakukan menggunakan layanan Pacil Web Service (PWS) yang disediakan untuk lingkungan akademis.

---

## Bagan Alur Request-Response Django

Diagram di bawah ini mengilustrasikan bagaimana sebuah permintaan dari pengguna (client) diproses oleh aplikasi Django hingga menghasilkan respons yang ditampilkan kembali ke pengguna.


**[Lihat Bagan Interaktif di Draw.io](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%22Ofzp7qnNFB__w1OHay2N%22%3E3ZpZd5s6EMc%2FDY%2FxAYnNj3Hc3D40PW3T05s8yqBg3bK4LF766e%2FISAaBbajX1C8JGi2gv2Z%2BGinR8EO0%2FCcls%2BlT4tNQQ7q%2F1PBYQ8hABoZf3LIqLY5tlYYgZb5oVBme2W8qjLqwFsynmdIwT5IwZzPV6CVxTL1csZE0TRZqs7ckVN86IwFtGZ49Erat%2FzI%2Fn5ZW19Ir%2B0fKgql8s6GLmojIxsKQTYmfLGom%2FEHDD2mS5OVTtHygIRdP6lL2e9xRu%2FmwlMZ5nw5fvfsfevb5%2B8vYeL4bzaavtvP1TowyJ2EhJqwhO4TxRj6bw2PAH4s0zAazlayBV9QqxeTylVQsTYrYp%2FylOlQvpiynzzPi8doF%2BAjYpnkUQsnY9J7TNKfLnfMyNmqBm9EkonkKH6OLDpYUWHiYMRTlRbVehmwzra2VLWxEuEiwGbpSER6EkH8gKuoj6lqEd6qooyqKnWsriluKRpw0pVdeWS1XFcu0ri2W2cf95owuDgpq4yKiGvZ7C%2BphH1UfQsYniB5HfOehaU914fWwn9GLKIvlBiyU7euu7rmENawtyjYFiv17vplDyQtJljFP1UWNeVAiXb3wwsA0HWl4BcOdPtAdJC3jZb3DeFUvfaEpg%2FnBEpbG8pOo38oWGrrDZydF6tFuT8pJGtC8a29ur2Ntoawt6yRtKQ1Jzubq525bPPGGLwnjnivdxBw2ArAZWOU0Ra962tEYqLmZGE5joFKH1kBrX9pM%2Bwj3svsE7jf6q6BZ3jdewQ0%2BkQmkuooXkpAFMXdRcAnuOCMeqAxyyXtRETHf52OMUpqx32SyHo9714zPfq2HNdKs8b5IF4mu6Kxt0su6J%2B6Js51cgNBApuMqa4VO4kqNDsnbW0bPs9Tu2Uhi1CmiD6wuhCxZ%2FlJ7rvWCUtWJF2SfExJGHpS6CGNelTCNxAnhQwmDG4RpblXnJkw7NXiisZd4yU8Sgx2OTxqPUptEfDsvf4IFGhXxf8VPePwB2diNUMbdSxnYfzHGagJynDedHyto2yH5OKxIPGyQ8CoZsxMPtaQGWQqNOlh0Qq6YPbmCr8kV1LgPwOhArqBG5oIunLlIN1O5EpBowtZ3bCQnt8GMjhMLMEN31cTkznn30Nh2Cj%2FVqcZ1VAIMhp0JybYzTYUhp84hfS%2BHTogT%2FDekKU0KYOtAnOAml%2FQL46R9zn6i0QR8Aozj24HJDm%2Bpjjm67RyJDzGWozIJI3WA88EF%2F1lGEicxX40MHCw%2FDDjDIVKB4x52i7L1XLQXN%2BuPfmRcn1PjB%2F0N%2BDF1lRqmcSB%2BNvfSEj%2FNC50z40dGx%2F57GJ7gBGRSxEF5diqTHN3neQ8vf%2Fz%2B9GnXJU1rMGmapE3LLd7v4P1ZFAcfkotwmvudC4Bu2%2BXdqbIo3XBUqFmQZZ71argTNcOrZjq7%2FpB67MHJMC%2BMGmdPpvONZrMkzuiNBL3dGfSuPDtdI8yhWP2HQ9m8%2Bj8R%2FOF%2F%3C%2Fdiagram%3E%3C%2Fmxfile%3E)**

**Penjelasan Bagan:**
1.  **Client Request**: Pengguna mengakses URL di browser.
2.  **urls.py**: Django menerima permintaan dan mencocokkan URL yang diminta dengan pola-pola yang terdaftar di `urls.py`. Jika cocok, Django akan meneruskannya ke fungsi *view* yang sesuai.
3.  **views.py**: Fungsi *view* menerima permintaan. Di sinilah logika bisnis utama berada. Jika perlu data, *view* akan berkomunikasi dengan `models.py`.
4.  **models.py & Database**: *Model* berfungsi sebagai jembatan ke database. Ia mengambil, membuat, atau memodifikasi data sesuai instruksi dari *view*.
5.  **View & Template (HTML)**: Setelah *view* mendapatkan data dari model, ia akan menggabungkan data tersebut dengan sebuah *template* HTML.
6.  **HTTP Response**: *View* merender *template* yang sudah terisi data menjadi halaman HTML utuh, lalu mengirimkannya kembali sebagai respons ke browser pengguna untuk ditampilkan.

---

## Penjelasan Konsep Kunci Django

### Apa Peran `settings.py`?
`settings.py` adalah **pusat kendali** atau jantung dari sebuah proyek Django. File ini berisi semua konfigurasi yang menentukan bagaimana aplikasi akan berjalan, termasuk:
- **Koneksi Database**: Jenis database yang digunakan, nama, user, dan password.
- **Aplikasi Terdaftar (`INSTALLED_APPS`)**: Daftar semua aplikasi yang aktif dalam proyek.
- **Middleware**: Komponen yang memproses request dan response secara global.
- **Konfigurasi File Statis**: Lokasi penyimpanan file CSS, JavaScript, dan gambar.
- **Secret Key**: Kunci kriptografi unik untuk keamanan proyek.

### Bagaimana Cara Kerja Migrasi Database?
Migrasi adalah cara Django untuk **menyinkronkan perubahan pada `models.py` dengan struktur tabel di database** secara otomatis dan terstruktur. Prosesnya terdiri dari dua langkah utama:
1.  `python manage.py makemigrations`: Django akan **mendeteksi perubahan** yang Anda buat pada `models.py` (misalnya menambah field baru) dan membuat sebuah file "resep" atau "cetak biru" di dalam folder `migrations/`. File ini berisi instruksi tentang bagaimana menerapkan perubahan tersebut.
2.  `python manage.py migrate`: Django akan membaca file-file "resep" dari `migrations/` yang belum diterapkan, lalu **mengeksekusinya** dengan menerjemahkannya menjadi perintah SQL. Perintah inilah yang secara nyata mengubah struktur tabel di database agar sesuai dengan model terbaru.

### Mengapa Django Cocok untuk Pemula?
Django sering dijadikan framework pilihan untuk memulai pembelajaran pengembangan web karena beberapa alasan kuat:
- **Banyak Fitur Bawaan (*Batteries Included*)**: Django sudah menyediakan banyak fungsionalitas umum seperti otentikasi pengguna, panel admin, dan ORM (Object-Relational Mapper) yang siap pakai, sehingga developer bisa fokus pada logika bisnis.
- **Cepat dan Efisien**: Dengan prinsip *Don't Repeat Yourself* (DRY), Django mendorong penulisan kode yang bersih dan dapat digunakan kembali, mempercepat proses pengembangan.
- **Aman (*Secure*)**: Django memiliki proteksi bawaan terhadap celah keamanan umum seperti *SQL injection*, *cross-site scripting* (XSS), dan *CSRF*, sehingga developer tidak perlu mengkhawatirkannya dari awal.
- **Skalabel (*Scalable*)**: Arsitekturnya yang modular memungkinkan aplikasi untuk tumbuh dari proyek kecil menjadi aplikasi berskala besar yang menangani traffic tinggi.
- **Open Source dan Komunitas Besar**: Django bersifat gratis dan didukung oleh komunitas yang sangat besar dan aktif, sehingga dokumentasi, tutorial, dan solusi atas masalah mudah ditemukan.