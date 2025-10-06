⚽ Wolverhampton Shop - Proyek Django

Selamat datang di repositori Wolverhampton Shop, sebuah aplikasi web e-commerce sederhana yang dibangun menggunakan framework Django. Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Pengembangan Berbasis Platform (PBP).

**[🔗 Tugas Individu 5](https://github.com/prasetyasurya-ui/football_shop/wiki/Tugas-Individu-5)**

## Tugas Individu 5

**[🔗 Kunjungi Aplikasi yang Sudah Deploy](https://prasetya-surya-footballshop.pbp.cs.ui.ac.id/)**

## Apa perbedaan antara synchronous request dan asynchronous request?

Untuk synchronous request, ketika mengirim permintaan ke server maka browser akan berhenti dan menunggu sampai server merespons sepenuhnya. Selama menunggu, user tidak bisa berinteraksi dengan halaman web sama sekali.

Untuk asynchronous request, browser mengirim permintaan di background sehingga browser tidak perlu menunggu respons. User tetap bisa berintaksi dengan halaman web sambil menunggu respons dari server tiba.

## Bagaimana AJAX bekerja di Django (alur request–response)?
Ajax (Asynchronous javascript and XML) bekerja dengan javascript mengirim request ke URL spesifik di server. Ketika permintaan diterima server, Django akan mencocokan URL dari request dengan view function yang sesuai. Setelah itu, Django akan memproses request dan mereturn response yaitu data dalam bentuk JSON. Javascript menerima response lalu memproses response tersebut dengan mengupdate halaman (DOM Manipulation).

## Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
1. User Experience yang lebih baik karena tidak ada flicker ketika page direload.
2. Karena asynchronous, bisa membuat fitur yang kompleks yang membuat loading lama tanpa membuat page website tidak bisa dipakai

## Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
1. Menggunakan CSRF Protection
2. Validasi form
3. Tidak memberi informasi sensitif di response yang direturn

## Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
1. Dengan tidak perlu reload halaman, maka experience user menggunakan web menjadi lebih mulus.
2. Interaksi dengan web, menggunakan ajax untuk memberi feedback ke user ketika suatu interaksi yang dilakukan error, sukses memberi pengalmaan yang lebih intuitif