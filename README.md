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

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/4b93017f-2337-42f5-8382-35d0d3cf015b)

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/c32f1016-5e08-4d1d-a5a1-1825bfb8a63b)

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cd47fc47-9257-4479-a468-9b941d495d7b)

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/1c5a4987-0488-4694-ba72-b251525d17d9)

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/a578b07d-fd57-42b2-aa8e-3c0989e7f330)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/dfd2b8c7-6fa3-42e8-9236-6d4e821c9a18)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/734beb86-5e1b-4e18-9970-46d067448c5a)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/275c7cfb-f865-4fd6-9866-477829c4ff1d)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/fa143d67-5333-4070-a438-3ad11ddcb305)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/461b5b37-58b0-4d44-a314-5c245a5647c6)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/bf40bf9f-4403-4570-b3f5-27b11b804d41)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cfa313c6-8204-4778-97a2-9467e0ec9419)

![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/83595692-2cf1-4a3d-9bf0-64c587713007)


4. Sorting Menggunakan QuickSort
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/644e3917-5dc3-49ed-955c-4cc0d3a0a1c9)

   


  
6. Searching Menggunakan JumpSearch
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/8ccb3cdc-76f6-44f3-b204-b3b2d8e385bc)

7. Fungsi

   def menu karyawan(): digunakan untuk menampilkan menu pilihan untuk melihat, 
   mengedit, mencari, dan mengurutkan tugas, serta melihat proyek update yang 
   tersedia.
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/ca45bfd7-e512-42cd-b7b8-3f05f2afe197)

   def menu manajer(): menampilkan menu pilihan untuk manajer, yang mencakup 
   operasi CRUD (Create, Read, Update, Delete) terhadap proyek, serta opsi 
   untuk kembali ke menu sebelumnya.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/f9912054-556f-4db5-bb68-4701085167e6)

   def menu crud proyek(): menampilkan menu crud proyek yang mencakup operasi CRUDS(Create, Read, Update, Delete, Searching) dan terdapat pilihan untuk masuk ke CRUD Tugas dan CRUD Proyek Update, dan pilihan 
   kembali kemenu sebelumnya.
  
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/0df873c6-5d0e-4354-90a3-219d9bd4f781)

   def menu crud tugas(): menampilkan menu crud tugas yang mencakup operasi 
   CRUDS(Create, Read, Update, Delete, Searching) dan pilihan kembali kemenu 
   sebelumnya.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/b37a06a0-dc39-4800-adc7-944d25a40aba)

   def menu crud proyek update(): menampilkan menu crud proyek update yang 
   mencakup operasi CRUDS(Create, Read, Update, Delete, Searching) dan pilihan 
   kembali kemenu sebelumnya.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/6fb36f0d-78b0-46e4-9c8e-be0a554ff476)

   def cek email manajer() : digunakan untuk memeriksa apakah seorang manajer 
   dengan alamat email tertentu sudah terdaftar dalam database. Fungsi ini 
   melakukan query ke database untuk mencari manajer dengan alamat email yang 
   diberikan, kemudian mengembalikan True jika manajer tersebut ditemukan dan 
   False jika tidak ditemukan.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/43e6fdc0-3b8b-4e33-8407-ab601264b097)

   def validasi login manajer() : digunakan untuk memvalidasi login manajer 
   berdasarkan email dan password yang diberikan. Fungsi ini melakukan query ke 
   database untuk mencocokkan email dan password dengan entri di tabel manajer. 
   Jika ada hasil yang sesuai, maka fungsi akan mengembalikan nilai True, 
   menandakan bahwa login berhasil. Jika tidak ada hasil yang sesuai, fungsi 
   akan mengembalikan nilai False, menandakan bahwa login gagal.

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/c7bc95ab-6f47-47ae-8838-5ca4b500b5fc)

   def ambil nama manajer() : mengambil nama manajer dari database berdasarkan 
   email dan ID manajer yang diberikan. Jika data manajer ditemukan sesuai 
   dengan email dan ID yang diberikan, maka fungsi ini mengembalikan nama 
   manajer. Jika tidak ditemukan, fungsi ini mengembalikan False.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/eb02f266-6e9c-4bfc-974d-ad9d26e189ed)

   def cek_email_karyawan():   digunakan untuk memeriksa apakah seorang 
   karyawan dengan email tertentu sudah terdaftar dalam database karyawan. 
   Fungsi ini melakukan query ke database untuk mencari data karyawan 
   berdasarkan email yang diberikan. Jika email karyawan tersebut ditemukan 
   dalam database, fungsi ini akan mengembalikan nilai True, yang menunjukkan 
   bahwa karyawan tersebut sudah terdaftar. Jika tidak ditemukan, maka fungsi 
   ini akan mengembalikan nilai False.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/bb8a5f49-72fb-4ffa-affd-e7c80c760b12)

   def validasi_login_karyawan(): digunakan untuk melakukan validasi login 
   karyawan dengan memeriksa apakah email dan password yang dimasukkan sesuai 
   dengan data yang ada dalam database. Jika data karyawan dengan email dan 
   password yang sesuai ditemukan, fungsi akan mengembalikan True, jika tidak 
   ditemukan, maka akan mengembalikan False.
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/9e43cb01-127d-4f2b-a615-ad887687665b)

   def ambil_nama_karyawan(): digunakan untuk mengambil nama karyawan 
   berdasarkan email dan ID karyawan yang diberikan. Fungsi ini menjalankan 
   query SQL untuk mencari entri karyawan yang sesuai dengan email dan ID 
   karyawan yang diberikan. Jika ada hasil yang sesuai, maka nama karyawan akan 
   diambil dari hasil query dan dikembalikan. Jika tidak ada hasil yang sesuai, 
   maka fungsi akan mengembalikan nilai False.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/eca90a43-9b70-4e5e-9a62-81d67ea26ffc)

   def menu_login(): digunakan untuk mengelola proses login ke dalam sistem. 
   Saat fungsi ini dijalankan, pengguna akan diminta untuk memilih apakah ingin 
   login sebagai karyawan atau manajer, atau keluar dari aplikasi. Setelah itu, 
   pengguna diminta untuk memasukkan email dan ID (untuk karyawan) atau ID 
   (untuk manajer) mereka. Jika informasi yang dimasukkan valid, pengguna akan 
   berhasil login dan diarahkan ke menu yang sesuai (menu karyawan atau menu 
   manajer). Jika informasi yang dimasukkan tidak valid atau tidak ditemukan, 
   pesan kesalahan akan ditampilkan.

   Penggunaan fungsi menu_login() akan menampilkan tampilan awal aplikasi, 
   diikuti dengan proses login ke dalam sistem.
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/5e5e6588-f597-4a95-aa20-1b18f79a725e)

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
