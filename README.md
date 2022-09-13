Link Aplikasi Heroku: https://pbp-katalog-natania.herokuapp.com/katalog/


Jawaban Pertanyaan:

I. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan Django](https://github.com/nataniadeandra/django-pbp-tugas/blob/main/static/bagan_django.png)

Pertama, request client akan dipetakan oleh URLS (urls.py) sesuai dengan path dari request tersebut. Setelah itu, request akan diteruskan ke view (views.py) untuk diproses. Selanjutnya, view akan meminta bantuan models (models.py) untuk membaca data dari database atau menulis ke database. Lalu, view akan memanggil template (katalog.html) untuk merender data sesuai dengan format file dan terakhir, hasil render akan dikembalikan dalam bentuk HTTP Response kepada client.


II. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual environment untuk memisahkan dependencies yang dibutuhkan untuk tiap project. Misalkan, project lama kita menggunakan Django versi yang lama, lalu muncul Django versi terbaru sehingga kita melakukan upgrade karena kita ingin membuat aplikasi lain dengan Django versi terbaru. Setelah itu, kita mencoba untuk menjalankan aplikasi lama kita, maka aplikasi kita tidak akan berjalan dengan baik karena terjadi banyak perubahan fungsi dari Django versi yang lama ke yang baru. Oleh karena itu, kita menggunakan virtual environment agar tiap project / aplikasi memiliki dependencies-nya masing-masing. Selain itu, apabila kita mengerjakan suatu project pada device yang berbeda atau mengerjakannya bersama-sama dengan orang lain dalam suatu tim, kita harus memastikan bahwa setiap device / setiap orang agar versi dari setiap dependencies yang digunakan sama. Namun, akan susah untuk memastikan hal di atas sehingga dibuatlah virtual environment untuk mengatasi masalah tersebut.

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi dependenices-nya tidak bisa kita tentukan secara spesifik untuk tiap project, melainkan mengikuti apa yang sudah ter-install pada device kita. Oleh karena itu, mungkin sedikit sulit apabila kita mengerjakan project dalam satu tim atau mengerjakannya pada device yang berbeda karena belum tentu versi dependencies yang ter-install pada device setiap orang sama. Apabila versi dari dependencies yang digunakan berbeda, maka belum tentu program dapat berjalan dengan baik. Oleh karena itu, meskipun tidak wajib, lebih baik untuk menggunakan virtual environment untuk tiap project yang berbeda.


III. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
Untuk melakukan pengambilan data dari database, kita perlu untuk meng-import models yang sudah ada. Lalu, kita gunakan method objects.all() untuk mendapatkan semua object dari class CatalogueItem. Untuk mengembalikan data ke dalam sebuah HTML, kita perlu membuat fungsi show_katalog yang menerima suatu request dan mengembalikan render(request, "katalog.html", context). Tampilan halaman HTML akan mengikuti katalog.html dan data pada variable context, yaitu list_barang, nama, dan npm, akan ikut di-render sehingga data tersebut bisa muncul pada halaman HTML.

2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
Implementasi routing pada urls.py terhadap fungsi pada views yaitu show_katalog yang telah dibuat agar halaman HTML dapat ditampilkan lewat browser dan menambahkan 'katalog' sebagai app_name serta menambahkan path('katalog/', include('katalog.urls')), pada urls.py yang ada pada folder project_django pada variable urlpatterns untuk mendaftarkan aplikasi katalog.

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
Mengganti kata "Fill me!" di bawah "Name: " dan "Student ID: " pada katalog.html menjadi {{nama}} dan {{npm}} agar menyesuaikan dengan data kita. Dibawah nama dan NPM, kita buat for loop menggunakan sintaks Django untuk mencetak untuk nama, harga, stok, rating, deskripsi, serta url dari setiap barang yang ada pada list_barang.

4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Membuat aplikasi baru pada Heroku, menambahkan api key dan app name pada repository secret, hubungkan aplikasi Heroku dengan repository GitHub, lalu deploy.