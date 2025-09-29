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

   * untuk views json:
   path('json/', show_json, name='show_json')

   * untuk views xml by id:
   path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id')
  
   * untuk views json by id:
   path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id')

   -Untuk membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek, saya membuat sebuah file bernama main.html di direktori templates di direktori main. Setelah itu saya mengedit template yang tersedia di web pbp. 
  Halaman main.html menampilkan daftar semua produk yang ada di database. Di bagian atas, terdapat informasi umum (nama aplikasi, nama mahasiswa, kelas) dan tombol “+ Add Product” untuk menuju halaman form penambahan produk. Jika belum ada produk, akan muncul pesan kosong. Jika ada, setiap produk ditampilkan dalam daftar berisi nama (bisa diklik ke detail), kategori, brand, stok, rating, harga, gambar thumbnail (jika ada), dan deskripsi singkat. Tiap produk juga memiliki tombol “Detail Produk” untuk melihat informasi lengkapnya.

   -Di direktori templates di dalam direktori main, saya membuat sebuah file bernama create_product. Halaman create_product.html ini menampilkan form untuk menambahkan produk baru ke database. Saat halaman dibuka, pengguna melihat judul “Add Product” di atas form. Form ini menggunakan metode POST agar data yang dikirim tidak muncul di URL dan dapat diproses oleh server. Di dalam form, terdapat {% csrf_token %} untuk mencegah serangan CSRF, lalu {{ form.as_table }} yang secara otomatis menampilkan semua field dari ProductForm dalam bentuk tabel. Setelah pengguna mengisi form dan menekan tombol “Add Product”, data akan dikirim ke server untuk divalidasi dan disimpan ke database.

  -Di direktori templates di dalam direktori main, saya membuat sebuah file bernama product_detail. Halaman product_detail.html ini menampilkan detail lengkap dari satu produk tertentu. Di bagian atas ada tombol “Back to Product List” untuk kembali ke halaman utama daftar produk. Setelah itu, halaman menampilkan nama produk, kategori, status featured (jika ada), brand, stok, rating, dan harga. Jika produk memiliki gambar thumbnail, gambar tersebut juga ditampilkan berukuran besar. Terakhir, deskripsi produk ditampilkan secara penuh tanpa dipotong.

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

Tugas 4:

1. AuthenticationForm di Django adalah form bawaan yang digunakan untuk proses login user, yaitu memvalidasi username dan password agar memastikan user terdaftar di database. Form ini biasanya dipakai bersama LoginView dan terintegrasi langsung dengan model User serta sistem autentikasi Django, sehingga mengurangi kode boilerplate dan sudah mendukung validasi keamanan seperti pengecekan password hash. Kelebihannya adalah siap pakai, aman, dan mudah diintegrasikan, namun kekurangannya form ini kurang fleksibel jika ingin login menggunakan field selain username, misalnya email, dan tampilan defaultnya perlu dikustomisasi.

2. Autentikasi dan otorisasi merupakan dua konsep berbeda namun saling terkait. Autentikasi adalah proses memastikan identitas user, misalnya login dengan username dan password, sedangkan otorisasi adalah proses menentukan hak akses user setelah identitasnya diketahui, misalnya user admin bisa menghapus data tetapi user biasa tidak. Django mengimplementasikan autentikasi melalui sistem django.contrib.auth dengan model User, fungsi login(), logout(), dan form AuthenticationForm, sementara otorisasi diimplementasikan menggunakan permissions, groups, dan decorators atau mixin seperti @login_required dan PermissionRequiredMixin untuk mengontrol akses ke resource tertentu.

3. Dalam konteks menyimpan state di aplikasi web, session dan cookies memiliki perbedaan mendasar. Session menyimpan data di server dan browser hanya menyimpan session ID, sehingga lebih aman dan bisa menyimpan banyak data, namun memerlukan storage server dan lebih berat jika aplikasi harus diskalakan. Cookies menyimpan data langsung di browser client, lebih sederhana dan tidak memerlukan storage server, namun ukurannya terbatas dan rentan dimanipulasi atau dicuri. Kelebihan session adalah keamanannya lebih tinggi dan fleksibel menyimpan data, sedangkan kekurangannya memerlukan penyimpanan server dan bisa membebani performa saat scale-out. Kelebihan cookies adalah sederhana dan ringan untuk server, sedangkan kekurangannya adalah risiko keamanan dan keterbatasan kapasitas data.

4. Penggunaan cookies tidak aman secara default karena data yang tersimpan di browser bisa dicuri atau dimanipulasi, misalnya melalui XSS, CSRF, atau session hijacking. Oleh karena itu, penggunaannya memerlukan kehati-hatian. Django menangani risiko ini dengan menandatangani cookies menggunakan opsi seperti SESSION_COOKIE_SECURE untuk memastikan cookies hanya dikirim melalui HTTPS, SESSION_COOKIE_HTTPONLY untuk mencegah akses melalui JavaScript, mendukung CSRF token untuk mencegah permintaan palsu, dan memungkinkan penyimpanan session di server melalui SESSION_ENGINE sehingga data sensitif tidak tersimpan langsung di client.

5. Langkah-langkah implementasi checklist di atas secara step-by-step:

   - Untuk membuat sistem autentikasi di Django, saya mengaktifkan virtual environment dan buka views.py di subdirektori main. Impor UserCreationForm, AuthenticationForm, messages, serta authenticate, login, dan logout. Kemudian, saya membuat fungsi register dengan UserCreationForm untuk membuat akun baru dan menampilkan pesan sukses, login_user dengan AuthenticationForm untuk autentikasi dan membuat session, serta logout_user untuk menghapus session dan redirect ke login. Setelah itu, saya membuat template register.html dan login.html menggunakan {{ form.as_table }} dan menampilkan pesan dari messages. Terakhir, di urls.py tambahkan path: register/, login/, dan logout/.

   - Saya membuat akun dengan cara memencet hyperlink register, kemudian mengisi data yang diminta, lalu setelah masuk, saya menambahkan 3 produk. Setelah itu saya membuat akun lain dan melakukan hal yang sama

   -Saya membuka `models.py` di subdirektori `main` dan menambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)` pada model `Product` agar setiap product terhubung dengan seller yang membuatnya; `null=True` memungkinkan product lama tetap valid, dan `on_delete=models.CASCADE` memastikan product ikut terhapus jika user dihapus. Setelah membuat migrasi dan menjalankannya, saya memodifikasi `views.py` pada fungsi `create_product` menggunakan `commit=False` agar bisa menambahkan field `user = request.user` sebelum menyimpan product ke database. Saya juga mengubah fungsi `show_main` untuk menampilkan product berdasarkan filter `all` atau `my` sesuai seller yang login, menampilkan username seller dan cookie `last_login`. Di template `main.html`, saya menambahkan tombol filter “All Product” dan “My Product”, tombol “+ Add Product”, serta tombol “Logout”, sementara di `product_detail.html` saya menampilkan seller product dengan `{{ product.user.username }}` atau “Anonymous” jika tidak ada. Setelah menjalankan server dan mencoba beberapa akun, saya memastikan setiap user hanya melihat product yang ia buat sendiri, sehingga mekanisme penghubungan product dengan seller berhasil diterapkan.

   -Saya menampilkan detail pengguna yang sedang login dengan mengakses request.user.username di view show_main, sehingga username user muncul di halaman utama. Selain itu, saya menyimpan waktu login terakhir ke cookie last_login di fungsi login_user menggunakan response.set_cookie('last_login', str(datetime.datetime.now())). Di halaman utama, saya mengambil nilai cookie tersebut dengan request.COOKIES.get('last_login', 'Never') dan menampilkannya di template, sehingga setiap kali saya login, username dan sesi login terakhir terlihat secara otomatis.

Tugas 5:
1. Jika terdapat beberapa CSS selector yang berlaku untuk suatu elemen HTML, maka browser akan menentukan urutan prioritas (specificity). Urutan prioritasnya adalah: (a) !important memiliki prioritas tertinggi, (b) inline style (ditulis langsung pada elemen dengan atribut style=""), (c) selector ID (#id), (d) selector class, atribut, dan pseudo-class (.class, [attr], :hover), dan terakhir (e) selector elemen dan pseudo-element (div, p, ::before). Jika terdapat selector dengan tingkat specificity yang sama, maka aturan yang ditulis terakhir dalam stylesheet akan dipakai (last rule wins). Dengan demikian, developer perlu berhati-hati agar tidak menumpuk aturan CSS yang bertabrakan.

2. Responsive design menjadi penting karena pengguna mengakses aplikasi web dari berbagai perangkat dengan ukuran layar berbeda, mulai dari smartphone, tablet, hingga desktop. Dengan responsive design, tampilan web akan menyesuaikan secara otomatis agar tetap nyaman dibaca dan mudah digunakan pada berbagai resolusi layar. Contoh aplikasi yang sudah menerapkan responsive design adalah YouTube, di mana tampilan video, menu, dan rekomendasi menyesuaikan ukuran layar secara dinamis. Sebaliknya, contoh aplikasi lama yang belum menerapkan responsive design adalah situs web pemerintah generasi lama yang hanya didesain untuk desktop, sehingga sulit diakses di perangkat mobile (misalnya tombol terlalu kecil atau layout rusak). Hal ini menunjukkan bahwa responsive design sangat krusial untuk memastikan pengalaman pengguna yang konsisten.

3. Margin, border, dan padding adalah bagian dari box model CSS. Margin adalah ruang di luar elemen, yang memberi jarak antar elemen. Border adalah garis tepi yang mengelilingi elemen, berada di antara margin dan padding. Padding adalah ruang di dalam elemen, yaitu jarak antara konten (teks atau gambar) dengan border. Implementasinya, misalnya:

div {
  margin: 20px;      /* jarak luar */
  border: 2px solid black;  /* garis tepi */
  padding: 10px;     /* jarak dalam */
}

Dengan kode ini, elemen div akan memiliki jarak luar 20px, border hitam 2px, dan ruang dalam 10px di sekitar konten.

4. Flexbox dan Grid Layout adalah dua sistem layout modern di CSS. Flexbox digunakan untuk mengatur elemen dalam satu dimensi (baris atau kolom). Kegunaannya adalah memudahkan penyusunan layout dinamis, seperti menyusun item menu horizontal atau menyejajarkan konten secara vertikal di tengah. Contoh: display: flex; justify-content: center; align-items: center;. Sementara itu, Grid Layout digunakan untuk mengatur elemen dalam dua dimensi (baris dan kolom) secara lebih kompleks. Kegunaannya adalah membangun struktur layout halaman web, seperti membuat tata letak dengan header, sidebar, konten utama, dan footer. Contoh: display: grid; grid-template-columns: 1fr 2fr; grid-template-rows: auto;. Dengan kombinasi keduanya, developer bisa membuat layout web yang responsif dan terorganisir dengan baik.

5. Cara implementasi step by step:
   -Untuk menambahkan fitur edit product, langkah pertama adalah membuat fungsi baru bernama edit_product di views.py. Fungsi ini menerima parameter request dan id, mengambil data product berdasarkan ID tersebut, lalu menampilkan form yang sudah otomatis terisi dengan data lama. Jika pengguna melakukan perubahan dan menekan tombol submit, data akan diperbarui di basis data, kemudian diarahkan kembali ke halaman utama. Setelah itu, dibuat template edit_product.html yang berisi form untuk menampilkan dan mengubah data. Selanjutnya, di urls.py, ditambahkan path khusus yang menghubungkan URL dengan fungsi edit_product. Terakhir, di dalam main.html, setiap item product dilengkapi dengan tombol edit yang hanya terlihat oleh pemilik product. 
   Untuk fitur delete product, prosesnya mirip dengan edit. Pertama, dibuat fungsi baru bernama delete_product di views.py yang bertugas menghapus data product berdasarkan ID, kemudian mengarahkan kembali ke halaman utama. Path baru ditambahkan di urls.py untuk menghubungkan URL dengan fungsi delete tersebut. Pada main.html, ditambahkan tombol delete di setiap card product yang hanya bisa diakses oleh pemiliknya.

   -Saya melakukan kustomisasi pada semua template yang diberikan. Untuk halaman login dan register, saya menerapkan background gradient dengan pattern grid yang menarik dan form dengan styling modern. Halaman tambah dan edit product didesain dengan card layout dan tombol dengan gradient yang konsisten. Halaman detail product dirancang dengan layout komprehensif yang menampilkan semua informasi penting dengan jelas dan terorganisir. Selain itu, saya juga menggunakan icon svg untuk memperbagus hasilnya.

   -Saya membuat halaman daftar product yang bisa menyesuaikan tampilan dengan dua kondisi berbeda. Kalau belum ada product, halaman akan menampilkan empty state yang menarik dengan pesan. Kalau sudah ada product, halaman menampilkan kumpulan card dalam grid yang responsif, sehingga layout tetap rapi di berbagai ukuran layar. Setiap card dirancang untuk menampilkan informasi produk secara jelas, dengan bagian khusus untuk thumbnail, konten, dan tombol aksi yang tersusun adaptif sesuai perangkat yang digunakan dengan menerapkan @mobile.

   -Saya membuat dua tombol edit dan delete pada setiap card product dengan menggunakan conditional statement {% if user.is_authenticated and product.user == user %} untuk memastikan hanya pemilik product yang dapat melihat tombol tersebut, dimana tombol edit menggunakan SVG icon pensil dengan styling cyan yang mengarah ke halaman edit product melalui {% url 'main:edit_product' product.id %}, sedangkan tombol delete menggunakan SVG icon trash can dengan styling merah yang mengarah ke fungsi hapus melalui {% url 'main:delete_product' product.id %}, dengan kedua tombol memiliki hover effects dan transitions untuk meningkatkan user experience serta ditempatkan dalam layout yang terorganisir di bagian bawah card product.

   -Saya membuat navbar yang responsive dengan membagi 2 designnya. Untuk tampilan desktop, navbar menampilkan menu horizontal dengan logo GoalMate, navigation links (Home dan Create Product), serta user section yang menampilkan informasi user dan tombol logout untuk user yang terautentikasi atau tombol login/register untuk anonymous users. Untuk tampilan mobile, saya mengimplementasikan hamburger menu button yang menggunakan JavaScript toggle functionality untuk menampilkan dan menyembunyikan menu vertikal, dimana semua fitur navigation dan user section diatur dalam layout vertical yang optimal untuk mobile devices.
