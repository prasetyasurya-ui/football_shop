⚽ Wolverhampton Shop - Proyek Django

Selamat datang di repositori Wolverhampton Shop, sebuah aplikasi web e-commerce sederhana yang dibangun menggunakan framework Django. Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Pengembangan Berbasis Platform (PBP).

**[🔗 Tugas Individu 4](https://github.com/prasetyasurya-ui/football_shop/wiki/Tugas-Individu-4)**

## Tugas Individu 5

**[🔗 Kunjungi Aplikasi yang Sudah Deploy](https://prasetya-surya-footballshop.pbp.cs.ui.ac.id/)**


# Langkah-Langkah Implementasi

##  Mengimplementasikan delete dan edit product
### Edit Product
membuat fungsi views `edit_product` yang menghandle pengeditan produk dan `edit_product.html` sebagai template render. Setelah itu routing untuk `edit_product` di `urls.py`
`edit_product`
```python
def edit_product(request, id):
    product = get_object_or_404(Item, pk = id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}

    return render(request, 'edit_product.html', context)
```

`edit_product.html`
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login - WolverHampton Shop</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-50 w-full min-h-screen flex items-center justify-center p-8">
    <div class="w-full max-w-md z-10 relative">
        <div class="bg-white p-6 rounded-lg shadow-sm form-style">
            <h1 class="text-center text-2xl font-bold">Join Us</h1>
            <h3 class="text-center mt-2 text-sm">Welcome to WolverHampton Shop</h3>
            <form method="POST" action="" class="space-y-8">
                {% csrf_token %}
                <div class="flex flex-col mb-2">
                    <label for="name" class="mb-2" >Username</label>
                    <input type="text"
                        maxlength="50"
                        name="username"
                        required
                        placeholder="Enter your username"
                        class="p-1 border px-4 py-3 rounded-md border-gray-300">
                </div>
                
                <div class="flex flex-col mb-2">
                    <label for="password1" class="mb-2" >Password</label>
                    <input 
                        type="password"
                        name="password1"
                        id="password"
                        placeholder="Enter your password"
                        class="p-1 border px-4 py-3 rounded-md border-gray-300">
                </div>

                <div class="flex flex-col mb-2">
                    <label for="password2" class="mb-2" >Confirm Password</label>
                    <input 
                        type="password"
                        name="password2"
                        id="password"
                        placeholder="Confirm your password"
                        class="p-1 border px-4 py-3 rounded-md border-gray-300">
                </div>

                <button type="submit" class="w-full bg-[#fdb913] px-3 py-3 rounded-lg font-bold hover:bg-[#e4a70d] transition-colors">Sign in</button>
            </form>
        
            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %} 
            <p class="mt-4 text-center p-2">Already have an account? <a href="{% url 'main:login' %}" class="text-[#fdb913] font-medium">Sign in</a></p>
            </div>
        </div>
    </div>

{% endblock content %}
```

### Delete Product
membuat fungsi views `delete_product` yang menghandle penghapusan produk dari basis data setelah itu routing untuk `delete_product` di `urls.py`
```python
def delete_product(request, id):
    product = get_object_or_404(Item, pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

## Kustomisasi desain
- Menggunakan Tailwind sebagai framework CSS
- Menkustomisasi `login`, `register`, `add product`, `edit product`, dan `detail product` page dengan Tailwind
- Membuat navbar untuk navigasi dan dibuat responsive untuk di screen yang kecil
- Membuat card untuk menampilkan preview product di main

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. Inline style, yaitu style yang ditulis langsung di element HTML
2. ID selectors, ID unik yang di elemen HTML
3. Class = Attribute = Pseudo-class, Class ditandai dengan deklarasi class di elemen HTML, attribute adalah menargetkan elemen yang memiliki atribut tersebut, Pseudo-class adalah status tertentu dari sebuah elemen seperti `:hover
4. ELement selectors = pseudo element, element selectors menargetkan semua elemen dari jenis tertentu, pseudo-element seperti `::before`

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
- Responsive design adalah konsep yang penting karena perangkat-perangkat digital di zaman sekarang memiiki ukuran layar yang berbeda-beda. Responsive design beradaptasi sesuai dengan ukuran layar yang digunakan oleh User, oleh karena itu user mendapat experience yang baik saat mengunjungi situs.

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
1. Padding adalah ruang transparan di dalam border, padding memberi jarak antara konten dengan border elemen itu sendiri. Cara mengimplementasikan => `padding: 20px` atau `padding: 10px 20px` atau `padding: 5px 6px 7px 8px`
2. Border adalah garis yang mengelilingi elemen. Cara Mengimplementasikan =>  `border: 1px solid red` atau `border: 1px`
3. Margin adalah ruang transparan di luar border, margin memberi jarak antara border elemen itu sendiri dengan elemen lain di sekitarnya. Cara mengimplementasikan => `margin: 5px` atau `margin: 0 auto` atau `margin: 10px 20px` atau `margin: 5px 6px 7px 8px`

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
1. Flexbox adalah sebuah model layout satu dimensi. Flexbox biasanya digunakan untuk mengatur, menyusun, dan mendistribusikan ruang di antara item-item dalam sebuah container (flex-container) secara horizontal ataupun vertikal. Kegunaan: Membuat navbar, menyusun list secara horizontal

2. Grid adalah sebuah model layout dua dimensi. Grid bisa menyusun elemen dalam baris dan kolom secara bersamaan. Kegunaan: membuat struktur page utama seperti header sidebar dan footer