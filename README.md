# Sistem Manajemen Proyek Perusahaan 

## Deskripsi Program

Program Manajemen Proyek Perusahaan adalah sistem yang dirancang untuk membantu manajer dalam perusahaan mengelola proyek. dengan program ini diharapkan dapat mendukung praktik industri yang terstruktur dan berkelanjutan. ini memungkinkan perusahaan untuk melakukan perencanaan, penjadwalan, alokasi sumber daya, monitoring, dan pelaporan progres proyek secara efisien dan efektif.

## Struktur Project

Project ini terdiri dari 3 file yaitu :
1. File Program

    Program utama yang berisikan kode program yang terhubung ke database untuk menjalankan sistem manajemen proyek perusahaan.

2. Database 

    Basis data sebagai tempat penyimpanan data yang akan digunakan dan diolah di dalam program manajemen proyek perusahaan.

3. Dokumentasi 

    Dokumentasi dari project dan program sistem manajemen proyek perusahaan yang sudah dirancang.

## Fitur dan Fungsionalitas

###### Library
1. Dalam pengembangan sistem ini, kami menggunakan beberapa library yang berperan
   penting dalam fungsionalitas sistem:
   -mysql.connector: Digunakan untuk menghubungkan program dengan database MySQL.
   -math: Digunakan untuk operasi matematika jika diperlukan dalam pengolahan data.
   -prettytable: Digunakan untuk memformat data dalam bentuk tabel agar lebih
   mudah dibaca.
   -time: Digunakan untuk operasi terkait waktu jika diperlukan dalam sistem.
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/35b9b8aa-b208-44df-bc20-c0292216b9c7)

2. Database yang digunakan dalam sistem ini adalah MySQL, yang di-hosting di
   db4free.net. Informasi login untuk database adalah sebagai berikut:
   Pengguna: 'tes123'
   Sandi: '123123123'
   Nama Database: 'manajemen_proyek'
   
3.Linked List yang kami gunakan terdiri dari beberapa method yaitu method tambah
  diakhir, ubah ke array, jump search proyek,tugas,proyek update, cari proyek,
  cari tugas, cari proyek update, tampilkan semua proyek, tugas, proyek update,
  tambah proyek, tugas ,proyek update, hapus proyek, tugas ,proyek update,
  perbarui tugas,proyek,proyek update,edit status, quick sort, sort proyek
  berdasarkan anggaran, sort tugas berdasarkan tenggat, sort proyek berdasarkan
  tanggal.
  
  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/1f105204-b8ac-4664-8bc4-9a98c989d197)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/ca4f2a33-c259-4c5b-b509-8a99f532f6ef)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/3d2aee73-a9f2-40e6-84b1-894b84da515a)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/d6b57a32-88b7-4f4c-af3b-4fc231323ccf)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/fb6582f7-3531-442a-a03b-119b2819dd93)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/8bf6b875-8770-4220-ab6d-32fb5198ad15)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/e8e5d39c-0067-446d-9f23-200a1a8f372c)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/f755e018-12ba-44bc-b643-db6cbdc20bbe)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/ae027db0-b864-4892-93b7-82b928e4d55a)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/f70677b6-e390-4f87-a37e-30e558df9993)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/0d303879-0762-4ad4-a036-dc013493d176)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/e3a984b7-0f44-44f0-886d-944731faf634)

4. Sorting Menggunakan QuickSort

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/18bdbedf-19c6-4927-8717-28c5bd2ee3a5)

5. Searching Menggunakan JumpSearch
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/6a0c490f-cdac-432d-8895-7edee0c935cf)

6. Fungsi
   def menu karyawan(): digunakan untuk menampilkan menu pilihan untuk melihat, mengedit, mencari, dan mengurutkan tugas, serta melihat proyek update yang tersedia.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/f2cee98a-a393-4448-8500-1fb6be4776e3)

   def menu manajer(): menampilkan menu pilihan untuk manajer, yang mencakup operasi CRUD (Create, Read, Update, Delete) terhadap proyek, serta opsi untuk kembali ke menu sebelumnya.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/edbca9e2-74c1-46a4-bb26-e7085a58b29d)

   def menu crud proyek(): menampilkan menu crud proyek yang mencakup operasi CRUDS(Create, Read, Update, Delete, Searching) dan terdapat pilihan untuk masuk ke CRUD Tugas dan CRUD Proyek Update, dan pilihan kembali kemenu sebelumnya.
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/085c677e-1e60-4429-b809-0069cb94b817)

   
   def menu crud tugas(): menampilkan menu crud tugas yang mencakup operasi CRUDS(Create, Read, Update, Delete, Searching) dan pilihan kembali kemenu sebelumnya

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/c4c3fdb5-15fe-4ca3-b7bd-a2f610f14b7d)

   def menu crud proyek update(): menampilkan menu crud proyek update yang mencakup operasi CRUDS(Create, Read, Update, Delete, Searching) dan pilihan kembali kemenu sebelumnya.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/725ff93e-6d23-41e4-a979-8f525da1420a)

   def cek email manajer() : digunakan untuk memeriksa apakah seorang manajer dengan alamat email tertentu sudah terdaftar dalam database. Fungsi ini melakukan query ke database untuk mencari manajer dengan alamat email yang diberikan, kemudian mengembalikan True jika manajer tersebut ditemukan dan False jika tidak ditemukan.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/26ae9e44-edbb-4a03-b45e-dfe901ae7096)
   def validasi login manajer() : digunakan untuk memvalidasi login manajer berdasarkan email dan password yang diberikan. Fungsi ini melakukan query ke database untuk mencocokkan email dan password dengan entri di tabel manajer. Jika ada hasil yang sesuai, maka fungsi akan mengembalikan nilai True, menandakan bahwa login berhasil. Jika tidak ada hasil yang sesuai, fungsi akan mengembalikan nilai False, menandakan bahwa login gagal.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/da8d7804-7c5a-4524-97d4-36a95b70fd6e)


   def ambil nama manajer() : mengambil nama manajer dari database berdasarkan email dan ID manajer yang diberikan. Jika data manajer ditemukan sesuai dengan email dan ID yang diberikan, maka fungsi ini mengembalikan nama manajer. Jika tidak ditemukan, fungsi ini mengembalikan False.
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/53ad8a82-094b-4e96-9b46-ab4dbf7a9ed2)

   def cek_email_karyawan():   digunakan untuk memeriksa apakah seorang karyawan dengan email tertentu sudah terdaftar dalam database karyawan. Fungsi ini melakukan query ke database untuk mencari data karyawan berdasarkan email yang diberikan. Jika email karyawan tersebut ditemukan dalam database, fungsi ini akan mengembalikan nilai True, yang menunjukkan bahwa karyawan tersebut sudah terdaftar. Jika tidak ditemukan, maka fungsi ini akan mengembalikan nilai False.
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/20eb7d41-9674-4a48-b820-5a43abb782cb)


   def validasi_login_karyawan(): digunakan untuk melakukan validasi login karyawan dengan memeriksa apakah email dan password yang dimasukkan sesuai dengan data yang ada dalam database. Jika data karyawan dengan email dan password yang sesuai ditemukan, fungsi akan mengembalikan True, jika tidak ditemukan, maka akan mengembalikan False.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/63688068-0f66-4599-aaec-df62ba30c5a3)

   def ambil_nama_karyawan(): digunakan untuk mengambil nama karyawan berdasarkan email dan ID karyawan yang diberikan. Fungsi ini menjalankan query SQL untuk mencari entri karyawan yang sesuai dengan email dan ID karyawan yang diberikan. Jika ada hasil yang sesuai, maka nama karyawan akan diambil dari hasil query dan dikembalikan. Jika tidak ada hasil yang sesuai, maka fungsi akan mengembalikan nilai False.
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/6912d1e6-c048-4172-b1d5-946d5a0348d7)


   def menu_login(): digunakan untuk mengelola proses login ke dalam sistem. Saat fungsi ini dijalankan, pengguna akan diminta untuk memilih apakah ingin login sebagai karyawan atau manajer, atau keluar dari aplikasi. Setelah itu, pengguna diminta untuk memasukkan email dan ID (untuk karyawan) atau ID (untuk manajer) mereka. Jika informasi yang dimasukkan valid, pengguna akan berhasil login dan diarahkan ke menu yang sesuai (menu karyawan atau menu manajer). Jika informasi yang dimasukkan tidak valid atau tidak ditemukan, pesan kesalahan akan ditampilkan.

Penggunaan fungsi menu_login() akan menampilkan tampilan awal aplikasi, diikuti dengan proses login ke dalam sistem.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/8b6d4bbd-7e5b-449a-9ab1-3ab49e31ffdd)


###### Manajer
- Pengelolaan Proyek
- Pengelolaan Proyek Update
- Pengelolaan Tugas
- Pengelolaan Karyawan

###### Karyawan
- Melihat Tugas
- Pengubahan Status Tugas
- Melihat Proyek Update

## Cara Penggunaan
