link website: https://rayyan-emir-goalmate.pbp.cs.ui.ac.id/

Tugas 2:

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
   
2. bagan : <img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/225a308a-b445-4055-a0c8-057895839668" />
   
   penjelasan:
   
   -Client mengirim request yang akan diterima oleh web server kemudian diteruskan ke django yang akan membaca konfigurasi settings.py yang kemudian diteruskan ke urls.py (1)
   
   -Django memeriksa urls.py untuk mencocokkan URL dengan pola yang ada. Jika cocok, maka Django meneruskan request ke fungsi view yang sesuai (2)
   
   -Fungsi view di views.py bertugas menangani request. Di sini ada pemanggilan data dari database lewat models.py (3), pengolahan logika,
    juga mengirimkan data ke template (4)
   
   -Jika view butuh data, models.py digunakan untuk mengambil (query) atau menyimpan data ke database. Hasil query ini akan dikembalikan ke views.py (5)
   
   -Data yang sudah diolah kemudian dirender oleh view ke dalam template HTML (6). Template ini bertugas menampilkan data dengan format yang rapi untuk user.
   
   -Template yang sudah dirender jadi halaman web dikirim kembali sebagai response (7), lalu tampil di browser user.

5. settings.py berperan sebagai pusat konfigurasi proyek Django, tempat semua pengaturan penting didefinisikan, mulai dari konfigurasi dasar seperti SECRET_KEY, DEBUG, dan ALLOWED_HOSTS, hingga pengaturan database, daftar aplikasi di INSTALLED_APPS, direktori template, middleware, serta lokasi file statis dan media.
   
6. Cara kerja migrasi di django adalah dengan membaca perubahan pada models.py, lalu membuat file migrasi menggunakan perintah makemigrations yang berisi instruksi perubahan struktur database (misalnya membuat tabel atau menambah kolom). Kemudian, perintah migrate mengeksekusi instruksi tersebut ke database sehingga model Python dan database selalu sinkron. Django juga menyimpan catatan migrasi agar setiap perubahan bisa dijalankan, dilacak, atau dibatalkan dengan aman.

7. Django cocok dijadikan permulaan belajar framework karena menyediakan fitur lengkap dan terstruktur seperti ORM, autentikasi, admin panel, template, dan routing tanpa perlu banyak library tambahan. Konsep arsitektur MVT-nya juga jelas sehingga membantu pemula memahami pemisahan antara data, logika, dan tampilan. Selain itu,django memiliki dokumentasi yang sangat baik serta komunitas yang besar sehingga memudahkan pencarian solusi.

8. Untuk asisten dosen pada tutorial 1 kerjanya sudah bagus. Saya sangat terbantu saat ada kesalahan karena bisa langsung menghubungi lewat voice chat discord.

Tugas 3:
1. Data delivery adalah proses mengirimkan data dari server ke client (misalnya browser atau aplikasi mobile) atau sebaliknya. Kita memerlukannya karena:

  -Interaksi real-time: Agar aplikasi dapat menampilkan data terbaru kepada pengguna tanpa harus melakukan refresh manual.

  -Integrasi antar sistem: Platform modern biasanya terdiri dari beberapa layanan (microservices), sehingga perlu data delivery untuk komunikasi antar layanan.

  -Pengalaman pengguna yang lebih baik: Pengiriman data yang efisien membuat aplikasi lebih responsif.

  -Keamanan dan kontrol data: Data delivery memungkinkan kita menerapkan autentikasi, otorisasi, dan validasi data sebelum sampai ke pengguna.

2. JSON lebih baik untuk kebanyakan aplikasi web modern karena:

  -Sintaks lebih ringkas dan mudah dibaca manusia dibanding XML yang verbose.

  -Lebih cepat diproses oleh browser atau JavaScript karena native support di JavaScript (JSON.parse, JSON.stringify).

  -Menghemat bandwidth karena ukuran file lebih kecil dibanding XML.

Walaupun begitu, XML masih digunakan jika:

  -Membutuhkan validation schema yang kompleks.

  -Interoperabilitas dengan sistem lama yang menggunakan XML.

Alasan popularitas JSON: ringkas, mudah diintegrasikan dengan JavaScript, efisien dalam ukuran dan parsing, cocok untuk REST API.

3. Fungsi is_valid() pada form Django:

  -Memeriksa validitas input dari user berdasarkan aturan yang ditentukan pada field (misal required, tipe data, panjang minimal/maksimal).

  -Membersihkan data (cleaned_data) sehingga bisa digunakan dengan aman.

Kita membutuhkan is_valid() karena:

  -Mencegah data tidak valid masuk ke database.

  -Menghindari error dan potensi bug ketika memproses data user.

  -Memudahkan pengelolaan feedback error kepada pengguna.

4. csrf_token digunakan untuk mencegah serangan CSRF (Cross-Site Request Forgery). CSRF terjadi ketika penyerang memanfaatkan sesi login pengguna untuk melakukan aksi yang tidak diinginkan tanpa sepengetahuan pengguna.Jika tidak menambahkan csrf_token, form akan rentan dieksploitasi, misalnya penyerang dapat membuat halaman jahat yang mengirim request ke aplikasi menggunakan kredensial pengguna yang sedang login. Akibatnya, data atau akun pengguna bisa dimanipulasi tanpa izin. Dengan csrf_token, setiap request POST memiliki token unik yang hanya diketahui server dan browser, sehingga request dari situs lain akan ditolak.

5. Cara mengimplementasikan checklist secara step-by-step:

  -import forms dan models dari main.forms dan main.models di file views.py dalam direktori main. Kemudian buat ke empat fungsi berikut:

    * untuk views xml:
    def show_xml(request):
      news_list = News.objects.all()
      xml_data = serializers.serialize("xml", news_list)
      return HttpResponse(xml_data, content_type="application/xml")

    * untuk views json:
    def show_json(request):
      news_list = News.objects.all()
      json_data = serializers.serialize("json", news_list)
      return HttpResponse(json_data, content_type="application/json")

    * untuk views xml by id:
    def show_xml_by_id(request, news_id):
      try:
          news_item = News.objects.filter(pk=news_id)
          xml_data = serializers.serialize("xml", news_item)
          return HttpResponse(xml_data, content_type="application/xml")
      except News.DoesNotExist:
          return HttpResponse(status=404) 
    
    * untuk views json by id:
    def show_json_by_id(request, news_id):
      try:
          news_item = News.objects.get(pk=news_id)
          json_data = serializers.serialize("json", [news_item])
          return HttpResponse(json_data, content_type="application/json")
      except News.DoesNotExist:
          return HttpResponse(status=404)

      #untuk views xml by id dan json by id menggunakan try except untuk menangani keadaan dimana data tidak tersedia

  -Untuk merouting URL masing masing views, kita hanya perlu mengimport fungsi-fungsi yang sudah kita buat sebelumnya dari main.views di main.urls, kemudian menambahkan path di dalam urlpatterns untuk masing-masing views.

  * untuk views xml:
  path('xml/', show_xml, name='show_xml')

  *untuk views json:
  path('json/', show_json, name='show_json')

  * untuk views xml by id:
  path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id')
  
  *untuk views json by id:
  path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id')

  -Untuk membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek, saya membuat sebuah file bernama main.html di direktori templates di direktori main. Setelah itu saya mengedit template yang tersedia di web pbp. 
  Halaman main.html menampilkan daftar semua produk yang ada di database. Di bagian atas, terdapat informasi umum (nama aplikasi, nama mahasiswa, kelas) dan tombol “+ Add Product” untuk menuju halaman form penambahan produk. Jika belum ada produk, akan muncul pesan kosong. 
  Jika ada, setiap produk ditampilkan dalam daftar berisi nama (bisa diklik ke detail), kategori, brand, stok, rating, harga, gambar thumbnail (jika ada), dan deskripsi singkat. Tiap produk juga memiliki tombol “Detail Produk” untuk melihat informasi lengkapnya.

  -Di direktori templates di dalam direktori main, saya membuat sebuah file bernama create_product. Halaman create_product.html ini menampilkan form untuk menambahkan produk baru ke database. Saat halaman dibuka, pengguna melihat judul “Add Product” di atas form. Form ini menggunakan metode POST agar data yang dikirim tidak muncul di URL dan dapat diproses oleh server. 
  Di dalam form, terdapat {% csrf_token %} untuk mencegah serangan CSRF, lalu {{ form.as_table }} yang secara otomatis menampilkan semua field dari ProductForm dalam bentuk tabel. Setelah pengguna mengisi form dan menekan tombol “Add Product”, data akan dikirim ke server untuk divalidasi dan disimpan ke database.

  -Di direktori templates di dalam direktori main, saya membuat sebuah file bernama product_detail.
  Halaman product_detail.html ini menampilkan detail lengkap dari satu produk tertentu. Di bagian atas ada tombol “Back to Product List” untuk kembali ke halaman utama daftar produk. 
  Setelah itu, halaman menampilkan nama produk, kategori, status featured (jika ada), brand, stok, rating, dan harga. Jika produk memiliki gambar thumbnail, gambar tersebut juga ditampilkan berukuran besar. Terakhir, deskripsi produk ditampilkan secara penuh tanpa dipotong.

-Tidak ada feedback, kerja asdos sudah bagus

6. Hasil SS :

   Xml:
   <img width="1387" height="812" alt="Image" src="https://github.com/user-attachments/assets/065ffeb4-05e7-4d3b-9ec1-6ccf4ac3e702" />

   Json:
   <img width="1467" height="793" alt="Image" src="https://github.com/user-attachments/assets/c30c2cfa-694f-486c-8510-ffdf0699aa85" />

   Xml by Id:
   <img width="1530" height="863" alt="Image" src="https://github.com/user-attachments/assets/3cc5491a-b2ee-416a-b191-ad05e7246276" />

   Json by Id:
   <img width="1530" height="863" alt="Image" src="https://github.com/user-attachments/assets/fba262c4-6c22-429f-b163-f04450ef83a8" />


    
