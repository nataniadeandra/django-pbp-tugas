<br>

## Link aplikasi Heroku:
https://pbp-katalog-natania.herokuapp.com/todolist/

<br><hr><br>

## Apa kegunaan {% csrf_token %} pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

<br>

<p>CSRF token digunakan untuk menghindari CSRF (Cross Site Request Forgery) attacks yang umum terjadi ketika user mengirimkan data ke website melalui forms. Kode CSRF token berupa kombinasi angka dan huruf yang di-generate oleh Django. CSRF token pada form Django berupa hidden form field. Ketika user masuk ke website untuk mengisi form, Django akan mengecek apakah CSRF tokennya sudah sesuai.</p>
<p>Jika tidak ada potongan kode {% csrf_token %}, maka CSRF (Cross Site Request Forgery) attacks akan lebih mudah terjadi sehingga menurunkan tingkat keamanan website.</p><br><hr><br>

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

<br>

Bisa, sebagai contoh pada login.html, untuk membuat form, kita menggunakan `<form>` dengan method="POST" dan untuk input dari form tersebut, kita menggunakan `<input>` dengan type="text" dan name="" di mana isi dari name disesuaikan dengan data yang akan diinput oleh user. Lalu, tambahkan button bagi user untuk men-submit data-data yang sudah di-input.

<br><hr><br>

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

<br>

<p>Setelah user memasukkan input pada form dan melakukan submisi, fungsi pada views.py yang telah dibuat sebelumnhya akan melakukan validasi input. Untuk form yang dibuat secara manual, kita dapat memvalidasinya menggunakan request.POST.get() di mana argumen di dalamnya disesuaikan dengan data yang diinput, lalu kita dapat menggunakan. Lain halnya untuk form yang menggunakan generator {{ form.as_table }}, kita dapat menggunakan fungsi is_valid() untuk validasi.</p>
<p>Setelah melakukan validasi, untuk menyimpan data ke database, kita dapat menggunakan form.save().</p>
<p>Untuk menampilkan data pada HTML, kita perlu mengambil data Task sesuai user dengan menggunakan objects.filter(user=request.user). Setelah itu masukkan data tersebut ke variabel context yang akan di-render. Pada template HTML, kita dapat menggunakan for loop yang sesuai dengan sintaks Django untuk menampilkan atribut dari tiap Task milik user tersebut.</p>

<br><hr><br>

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

<br>

1. Masuk ke directory project, nyalakan environment, lalu jalankan
    ```
    django-admin startapp todolist
    ```

2. Menambahkan
    ```
    'todolist'
    ```
    pada INSTALLED_APPS di settings.py dan menambahkan
    ```
    path('todolist/', include('todolist.urls'))
    ```
    pada urlpatterns di urls.py pada folder project_django.

3. Membuat class Task pada models.py dan meng-import models serta menambahkan models. Model sebagai argumen pada class MyWatchList untuk menandakan bahwa class akan dipakai sebagai model. Selain itu, kita juga perlu membuat atribut dari class tersebut dan menyesuaikan field-nya dengan tipe data dari atribut tersebut. Setelah itu, lakukan:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Pada views.py buat fungsi-fungsi berikut:
    ```
    I. login_user

    Fungsi login_user akan mendapatkan username dan password berdasarkan input user menggunakan request.POST.get() lalu melakukan autentikasi untuk mendapatkan user yang sesuai dengan username dan passwordnya. Apabila user tersebut ada, maka user akan ter-login dan program akan me-redirect user ke halaman show_todolist.
    ```
    ```
    II. logout_user

    Fungsi logout_user akan me-logout user dan me-redirect user kembali ke halaman login.
    ```
    ```
    III. register

    Fungsi register menggunakan UserCreationForm() untuk membuat suatu user baru. Setelah itu, fungsi akan memvalidasi username dan password dari user baru menggunakan is_valid(). Jika validasi sukses, maka fungsi akan menggunakan form.save() untuk menyimpan user baru ke database. Setelah itu fungsi akan menampilkan pesan bahwa pembuatan akun sukses dan user akan ter-redirect ke halaman login.
    ```
    ```
    IV. create_task

    Fungsi create_task akan membuat form berdasarkan ModelForm TaskForm yang ada di forms.py. Setelah meminta input user, fungsi akan melakukan validasi dengan menggunakan is_valid(). Jika form valid, maka fungsi akan menambahkan user sesuai dengan user yang sekarang ter-login dan tanggal dibuatnya task sesuai dengan tanggal hari ini. Setelah itu, data akan disimpan ke database dan user akan ter-redirect ke halaman show_todolist.
    ```

5. Membuat file todolist.html yang akan ditampilkan ketika user mengakses halaman utama todolist. Untuk tombol tambah task baru dan tombol logout, kita dapat menggunakan `<button>` serta untuk menampilkan tanggal pembuatan task, judul task, dan deskripsi task, kita dapat menggunakan for loop. Username pengguna (didapat dari request.user) dan atribut dari Task (didapat menggunakan fungsi objects.filter(user=request.user)) akan dimuat ke dalam context pada fungsi show_todolist di views.py untuk di-render sesuai dengan template HTML.

6. Buat file forms.py, lalu di dalam file tersebut buat suatu class sebagai berikut:
    ```
    class TaskForm(ModelForm):
        class Meta:
            model = Task
            fields = (
                'title',
                'description',
            )
    ```
    form di atas akan mengikuti model Task dengan field pertama sebagai judul dan field kedua sebagai deskripsi, lalu pada views.py buat fungsi berikut:
    ```
    def create_task(request):
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.date = date.today()
                instance.save()
                return redirect('todolist:show_todolist')
        else:
            form = TaskForm()

        context = {
            'form': form,
        }

        return render(request, 'create_task.html', context)
    ```
    fungsi di atas akan mengecek apakah request merupakan request POST, jika iya maka fungsi akan membuat suatu instance TaskForm dengan argumen request lalu jika form valid, fungsi akan menambahkan user dan tanggal, lalu akan di-save dan kembali ke halaman show_todolist. Jika bukan request POST, maka fungsi hanya akan membuat suatu form kosong. Setelah itu, kita buat variabel context berisi jawaban form. Setelah itu, fungsi akan mereturn hasil render sesuai dengan template create_task.html.

7. Pada urls.py import fungsi yang sudah dibuat sebelumnya tambahkan path url ke dalam urlpatterns, yaitu:
    ```
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    ```
    untuk mengakses fungsi yang sudah di-import sebelumnya.

8. Karena aplikasi sudah ada pada Heroku, API key beserta app name sudah ditambahkan juga sebelumnya pada repository secret, dan aplikasi Heroku sudah terhubung dengan repository GitHub, kita hanya cukup men-deploy-nya saja.

9. Masuk ke link aplikasi todolist yang sudah di-deploy. Lalu buat 2 akun. Untuk masing-masing akun, masukkan username dan password, untuk aplikasi ini:
    ```
    Akun pertama
    Username: dummySatu
    Password: jibe8vCRLFkNhKT

    Akun kedua
    Username: dummyDua
    Password: MKQQumZ2KQJQA8w
    ```
    Setelah membuat akun, login ke masing-masing akun dan create 3 tasks untuk masing-masing akun.