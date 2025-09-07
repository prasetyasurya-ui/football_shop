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

### 2. Konfigurasi dan Proyek
- Mengonfigurasi environment variable lokal dan production
- Memodifikasi settings.py untuk menggunakan database, environment variables, dan menambahkan localhost dan 127.0.0.1 di allowed hosts untuk keperluan development

### 3. Deployment
Aplikasi yang sudah selesai dikembangkan kemudian di-deploy agar bisa diakses secara publik.
- Deploy menggunakan python `manage.py migrate` dan `python manage.py runserver`
- Upload proyek ke github untuk keperluan version control

---

## Pembuatan Aplikasi `main`
Aplikasi inti bernama `main` dibuat untuk menangani fungsionalitas utama toko.
- Membuat app main dengan command `python manage.py startapp main` dan daftarkan ke installed Apps di settings.py

## Melakukan Routing pada proyek agar dapat menjalankan aplikasi main
- Menambahkan `include('main.urls')` di urls.py yang berada di direktori proyek agar mengimpor rute URL yang berada di main.urls dan karena path nya berupa string kosong maka show_main (fungsi di views.py) akan dijalankan dari perintah di urls.py yang berada di direktori main dan maka dari itu menjalankan aplikasi main

## Membuat model pada aplikasi main dengan nama product dan memiliki atribut wajib
- Mengimport UUID untuk Id Produk
- Membuat class Produk untuk pembuatan produk dengan atribut atribut wajib dan tipe yang sesuai

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
- membuat fungsi `show_main` yang akan merender html dari `main.html` dengan fungsi django

## Nembuat sebuah routing pada urls.py pada aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
- Membuat urls.py dalam direktori main yang berisi perintah untuk mengeksekusi suatu fungsi view di main.views apabila berada di root proyek

## Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Hubungkan projek dengan git
- Mendeploy menggunakan pacil-web-service (pws)

---

## Bagan Alur Request-Response Django

Diagram di bawah ini mengilustrasikan bagaimana sebuah permintaan dari pengguna (client) diproses oleh aplikasi Django hingga menghasilkan respons yang ditampilkan kembali ke pengguna.

**[Lihat Bagan Interaktif di Draw.io](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%22Ofzp7qnNFB__w1OHay2N%22%3E3ZpZd5s6EMc%2FDY%2FxAYnNj3Hc3D40PW3T05s8yqBg3bK4LF766e%2FISAaBbajX1C8JGi2gv2Z%2BGinR8EO0%2FCcls%2BlT4tNQQ7q%2F1PBYQ8hABoZf3LIqLY5tlYYgZb5oVBme2W8qjLqwFsynmdIwT5IwZzPV6CVxTL1csZE0TRZqs7ckVN86IwFtGZ49Erat%2FzI%2Fn5ZW19Ir%2B0fKgql8s6GLmojIxsKQTYmfLGom%2FEHDD2mS5OVTtHygIRdP6lL2e9xRu%2FmwlMZ5nw5fvfsfevb5%2B8vYeL4bzaavtvP1TowyJ2EhJqwhO4TxRj6bw2PAH4s0zAazlayBV9QqxeTylVQsTYrYp%2FylOlQvpiynzzPi8doF%2BAjYpnkUQsnY9J7TNKfLnfMyNmqBm9EkonkKH6OLDpYUWHiYMRTlRbVehmwzra2VLWxEuEiwGbpSER6EkH8gKuoj6lqEd6qooyqKnWsriluKRpw0pVdeWS1XFcu0ri2W2cf95owuDgpq4yKiGvZ7C%2BphH1UfQsYniB5HfOehaU914fWwn9GLKIvlBiyU7euu7rmENawtyjYFiv17vplDyQtJljFP1UWNeVAiXb3wwsA0HWl4BcOdPtAdJC3jZb3DeFUvfaEpg%2FnBEpbG8pOo38oWGrrDZydF6tFuT8pJGtC8a29ur2Ntoawt6yRtKQ1Jzubq525bPPGGLwnjnivdxBw2ArAZWOU0Ra962tEYqLmZGE5joFKH1kBrX9pM%2Bwj3svsE7jf6q6BZ3jdewQ0%2BkQmkuooXkpAFMXdRcAnuOCMeqAxyyXtRETHf52OMUpqx32SyHo9714zPfq2HNdKs8b5IF4mu6Kxt0su6J%2B6Js51cgNBApuMqa4VO4kqNDsnbW0bPs9Tu2Uhi1CmiD6wuhCxZ%2FlJ7rvWCUtWJF2SfExJGHpS6CGNelTCNxAnhQwmDG4RpblXnJkw7NXiisZd4yU8Sgx2OTxqPUptEfDsvf4IFGhXxf8VPePwB2diNUMbdSxnYfzHGagJynDedHyto2yH5OKxIPGyQ8CoZsxMPtaQGWQqNOlh0Qq6YPbmCr8kV1LgPwOhArqBG5oIunLlIN1O5EpBowtZ3bCQnt8GMjhMLMEN31cTkznn30Nh2Cj%2FVqcZ1VAIMhp0JybYzTYUhp84hfS%2BHTogT%2FDekKU0KYOtAnOAml%2FQL46R9zn6i0QR8Aozj24HJDm%2Bpjjm67RyJDzGWozIJI3WA88EF%2F1lGEicxX40MHCw%2FDDjDIVKB4x52i7L1XLQXN%2BuPfmRcn1PjB%2F0N%2BDF1lRqmcSB%2BNvfSEj%2FNC50z40dGx%2F57GJ7gBGRSxEF5diqTHN3neQ8vf%2Fz%2B9GnXJU1rMGmapE3LLd7v4P1ZFAcfkotwmvudC4Bu2%2BXdqbIo3XBUqFmQZZ71argTNcOrZjq7%2FpB67MHJMC%2BMGmdPpvONZrMkzuiNBL3dGfSuPDtdI8yhWP2HQ9m8%2Bj8R%2FOF%2F%3C%2Fdiagram%3E%3C%2Fmxfile%3E)**

**Penjelasan Bagan:**
1. Pengguna mengakses URL di browser -> (urls.py) Django menerima permintaan dan mencocokkan URL yang diminta dengan pola-pola yang terdapat di `urls.py`. Jika cocok, Django akan meneruskannya ke fungsi view yang sesuai.
2. (views.py) menerima request. Jika perlu data, view akan berkomunikasi dengan `models.py`
3. (models.py) berfungsi sebagai jembatan ke database. Ia mengambil, membuat, atau memodifikasi data sesuai dengan instruksi dari `views.py`
4. Setelah `views.py` mendapat data dari model, ia akan menggabungkan data tersebut dengan template HTML atau di projek ini `template.html`
5. `views.py` akan merender`template tersebut menjadi halaman HTML yang utuh lalu mengirimkannya kembali sebagai respon ke browser pengguna untuk ditampilkan

---

## Penjelasan Konsep Kunci Django

### Apa Peran `settings.py`?
- `settings.py` adalah pusat kendali dari proyek django yang menentukan bagaimana proyek django akan berjalan

### Bagaimana Cara Kerja Migrasi Database di Django?
- Menyinkronkan struktur tabel basis data dengan perubahan model yang terbaru
- Pada saat menjalankan `python manage.py makemigrations`, django melihat file models.py dan membandingkannya dengan migrasi sebelumnya untuk mendeteksi perubahan.
- Pada saat menjalankan `python manage.py migrate`, django menerapkan perubahan pada database menggunakan perintah SQL agar sinkron dengan file models.py

### Mengapa Django Cocok untuk Pemula?
- Karena django memiliki banyak built-in feature
- Cepat
- Open Source
- Secure
- Scalable

