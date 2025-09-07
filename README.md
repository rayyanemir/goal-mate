link website: https://rayyan-emir-goalmate.pbp.cs.ui.ac.id/

1. Cara mengimplementasikan checklist secara step-by-step:
   -Setelah mendownload dependencies yang dibutuhkan, saya membuat aplikasi Django baru dengan menggunakan kode:
     django-admin startproject <nama-project>
   -Setelah menyiapkan konfigurasi Environment Variables dan juga konfigurasi di dalam aplikasi, serta menjalankan server, saya membuat aplikasi main dengan kode:
     python manage.py startapp main
     kemudian mendaftarkan aplikasi main ke dalam proyek dengan membuka direktori settings.py dan memasukan 'main' di variabel INSTALLED_APPS
   -Untuk melakukan routing pada proyek, buka urls.py di direktori utama (level proyek), lalu impor fungsi include dari django.urls.
    Setelah itu tambahkan baris path('', include('main.urls')) ke dalam variabel urlpatterns agar URL root diarahkan ke aplikasi main.
   -Untuk membuat model, di file models.py saya membuat class product, lalu memasukan kategori, atribut wajib, beberapa atribut yang saya tambahkan, serta property.
    Setelah itu migrasikan.
   -Pada views.py, buat fungsi show_main(request) yang mengembalikan template HTML beserta data yang ingin ditampilkan (nama aplikasi, nama, dan kelas).
   -Untuk melakukan routing pada aplikasi main, buka urls.py di folder aplikasi main, lalu impor fungsi path dari django.urls dan fungsi view show_main dari main.views.
    Setelah itu tambahkan baris path('', show_main, name='show_main') ke dalam variabel urlpatterns agar URL root aplikasi memanggil view show_main.
   -Untuk deploy, masukan:
    git push origin master
    git push pws master
   
2. link : https://www.canva.com/design/DAGyT7DboN4/vR_5s-HFtxhxsw6mxeHxhg/edit?utm_content=DAGyT7DboN4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
   penjelasan:
   -Client mengirim request yang akan diterima oleh web server kemudian diteruskan ke django yang akan membaca konfigurasi settings.py yang kemudian diteruskan ke urls.py (1)
   -Django memeriksa urls.py untuk mencocokkan URL dengan pola yang ada. Jika cocok, maka Django meneruskan request ke fungsi view yang sesuai (2)
   -Fungsi view di views.py bertugas menangani request. Di sini ada pemanggilan data dari database lewat models.py (3), pengolahan logika,
    juga mengirimkan data ke template (4)
   -Jika view butuh data, models.py digunakan untuk mengambil (query) atau menyimpan data ke database. Hasil query ini akan dikembalikan ke views.py (5)
   -Data yang sudah diolah kemudian dirender oleh view ke dalam template HTML (6). Template ini bertugas menampilkan data dengan format yang rapi untuk user.
   -Template yang sudah dirender jadi halaman web dikirim kembali sebagai response (7), lalu tampil di browser user.

3. settings.py berperan sebagai pusat konfigurasi proyek Django, tempat semua pengaturan penting didefinisikan, mulai dari konfigurasi dasar seperti SECRET_KEY, DEBUG, dan ALLOWED_HOSTS,
   hingga pengaturan database, daftar aplikasi di INSTALLED_APPS, direktori template, middleware, serta lokasi file statis dan media.
   
4. Cara kerja migrasi di django adalah dengan membaca perubahan pada models.py, lalu membuat file migrasi menggunakan perintah makemigrations yang berisi instruksi perubahan struktur database (misalnya membuat tabel atau menambah kolom).
   Kemudian, perintah migrate mengeksekusi instruksi tersebut ke database sehingga model Python dan database selalu sinkron. Django juga menyimpan catatan migrasi agar setiap perubahan bisa dijalankan, dilacak, atau dibatalkan dengan aman.

5. Django cocok dijadikan permulaan belajar framework karena menyediakan fitur lengkap dan terstruktur seperti ORM, autentikasi, admin panel, template, dan routing tanpa perlu banyak library tambahan.
   Konsep arsitektur MVT-nya juga jelas sehingga membantu pemula memahami pemisahan antara data, logika, dan tampilan. Selain itu,d jango memiliki dokumentasi yang sangat baik serta komunitas yang besar sehingga memudahkan pencarian solusi.

6. Untuk asisten dosen pada tutorial 1 kerjanya sudah bagus. Saya sangat terbantu saat ada kesalahan karena bisa langsung menghubungi lewat voice chat zoom.

    
