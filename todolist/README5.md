
## Link aplikasi Heroku:
https://pbp-katalog-natania.herokuapp.com/todolist/

<br>
<hr>

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

<h2>1. Inline CSS</h2>

Dalam Inline CSS, kita meletakkan property CSS pada attribute tag HTML, sebagai contoh:
```
<h1 style="color:blue;text-align:center;">Hello</h1>
```
<h3>Kelebihan: </h3>

- Dapat mengkostumisasi tiap element tanpa memikirkan dampaknya pada elemen lain

<h3>Kekurangan: </h3>

- Attribute dari tiap elemen akan menjadi sangat panjang
- Mungkin terjadi banyak pengulangan

<br>

<h2>2. Internal CSS</h2>

Dalam Internal CSS, attribute CSS ditulis di dalam tag `<style>` pada file HTML.

<h3>Kelebihan</h3>

- Tidak perlu membuat file HTML dan seluruh attribute CSS menjadi satu kesatuan

<h3>Kekurangan</h3>

- Dokumen dapat menjadi kurang bersih karena attribute CSS bercampur dengan dokumen HTML

<br>

<h2>3. External CSS</h2>

Dalam external CSS, attribute CSS ditulis di luar file HTML. Hal ini bisa dilakukan dengan membuat file .css baru, lalu import ke file HTML, sebagai berikut:
```
<link rel="stylesheet" href="example.css"/>
```

<h3>Kelebihan</h3>

- Dapat membuat banyak properti

<h3>Kekurangan</h3>

- Cenderung kompleks dan kurang efektif untuk dokumen singkat

<br>
<hr>

## Jelaskan tag HTML5 yang kamu ketahui.

<br>

1. `<head>` berisi informasi terkait dokumen
2. `<body>` menyatakan isi dari dokumen
3. `<h1>` hingga `<h6>` melambangkan headings mulai dari yang terbesar hingga terkecil
4. `<img>` merepresentasikan gambar atau foto
5. `<button>` untuk tombol
6. `<br>` untuk line break atau baris kosong
7. `<hr>` untuk garis horizontal
8. `<p>` untuk paragraf
9. `<form>` untuk form
10. `<input>` untuk menerima input dari user
11. `<div>` yang melambangkan bagian tertentu dari dokumen

<br>
<hr>

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

<br>

1. Tag -> memilih elemen berdasarkan tag
    ```
    p {
        lines of code
    }
    ```
    Potongan kode di atas akan menyeleksi semua elemen dengan tag `<p>`.

2. Class -> memilih elemen berdasarkan class
    ```
    .class-example {
        lines of code
    }

    ```
    Potongan kode di atas akan menyeleksi semua elemen dengan class="class-example".

3. ID -> memilih elemen berdasarkan ID
    ```
    #id-example {
        lines of code
    }
    ```
    Potongan kode di atas akan menyeleksi semua elemen dengan id="id-example".

4. Attribute -> memilih elemen berdasarkan attribute mana saja
    ```
    [attribute-example] {
        lines of code
    }
    ```
    Potongan kode di atas akan menyeleksi semua elemen yang memiliki attribute-example sebagai salah satu attribute-nya.

5. Keseluruhan
    ```
    * {
        lines of code
    }
    ```
    Potongan kode di atas akan menyeleksi seluruh elemen pada dokumen.

6. Pseudo<br>
    a. Pseudo-class
    ```
    example:hover {
        lines of code
    }
    ```
    Potongan kode di atas merepresentasikan elemen dengan tag example ketika di-hover.<br>
    b. Pseudo-element
    ```
    example span {
        lines of code
    }
    ```
    Potongan kode di atas akan menyeleksi semua elemen span di dalam elemen tag example.

<br>
<hr>

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

<br>

1. Pada folder templates, buat file _header.html untuk styling menggunakan CSS. Styling ditulis di dalam tag `<style>` dan tidak lupa untuk meng-import bootstrap.
2. Pada folder templates, isi file base.html dengan navigation bar untuk tiap halaman dan tambahkan styling.
3. Tambahkan styling juga untuk create_task.html, login.html, register.html, dan todolist.html.
4. Menambahkan widgets pada forms.py untuk mengatur lebar dan panjang dari text area deskripsi task.
5. Pada todolist.html buat cards untuk tiap task-nya.
6. Push lalu deploy ke Heroku.

<br>