## Link Aplikasi Heroku
https://pbp-katalog-natania.herokuapp.com/todolist/

<hr>

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

<br>

Dalam asynchronous programming, beberapa request dapat berjalan secara paralel atau bersamaan. Request baru tidak perlu menunggu request sebelumnya untuk selesai agar request baru tersebut bisa dijalankan. Berbeda dengan synchronous programming di mana apabila terdapat request baru, request tersebut harus menunggu request sebelumnya selesai sebelum request baru dijalankan.

<hr>

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

<br>

Event-driven programming merupakan suatu paradigma di mana jalannya program ditentukan oleh tindakan pengguna. Sesuai dengan namanya, event-driven berarti alur program berjalan sebagaimana mestinya karena suatu peristiwa.

Contoh: button add task yang membuka modal berisi form

<hr>

## Jelaskan penerapan asynchronous programming pada AJAX.

<br>

AJAX akan meminta file dalam bentuk JavaScript dan XML agar mudah diurai sehingga mengurangi waktu load dan meningkatkan kinerja web. AJAX akan menjalankan protokol HTTP dan mendapatkan semua kata kerja HTTP. tidak terkecuali permintaan HEAD. Permintaan di atas memungkinakn data diperbarui secara real-time dan dengan ini, menghapus interaksi sinkron antara sisi klien dan sisi server default yang memerlukan proses dijalankannya request secara berkala.

<hr>

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

<br>

1. Buat view show_json
2. Buat fungsi menggunakan AJAX untuk mendapatkan data dari view yang sudah kita buat sebelumnya
3. Tambahkan modal dan buat tombol add task yang berfungsi untuk memunculkan modal tersebut
4. Isi modal dengan form yang sesuai, yaitu form untuk membuat object Task
5. Buat function AJAX yang bersesuaian:
    - showModal(): untuk menampilkan modal
    - showTask(data): untuk menampilkan seluruh data
    - showLastTask(data): untuk menampikan data yang baru saja ditambahkan melalui modal
    - submitForm(): mendapatkan data pada modal dan menampilkannya
6. Deploy ke heroku