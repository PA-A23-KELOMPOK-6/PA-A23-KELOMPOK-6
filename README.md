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

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/21be3fe5-d80e-436f-9bc1-dbfe20381821)


3. Linked List yang kami gunakan terdiri dari beberapa method yaitu method tambah  diakhir, jump search,tugas,proyek update, cari proyek,cari tugas, cari proyek update, tampilkan semua
   proyek, tugas, proyek update,tambah proyek, tugas ,proyek update, hapus proyek, tugas ,proyek update, perbarui tugas,proyek,proyek update,edit status, quick sort, sort proyek berdasarkan anggaran, sort 
   tugas berdasarkan tenggat, sort proyek berdasarkan tanggal.

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/966a5d69-00c9-47ce-b3e9-3b5adebdbab2)

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
  
5. Searching Menggunakan JumpSearch
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/e07f6fb5-868b-42bb-84e6-f6cc47470b9d)


6. Fungsi

   - def menu karyawan(): digunakan untuk menampilkan menu pilihan untuk melihat, mengedit, mencari, dan mengurutkan tugas, serta melihat proyek update yang  tersedia.
   
     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/ca45bfd7-e512-42cd-b7b8-3f05f2afe197)

   - def menu manajer(): menampilkan menu pilihan untuk manajer, yang mencakup operasi CRUD (Create, Read, Update, Delete) terhadap proyek, serta opsi untuk kembali ke menu sebelumnya.
   
     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/f9912054-556f-4db5-bb68-4701085167e6)

   - def menu crud proyek(): menampilkan menu crud proyek yang mencakup operasi CRUDS(Create, Read, Update, Delete, Searching) dan terdapat pilihan untuk masuk ke CRUD Tugas dan CRUD Proyek Update, dan 
     pilihan kembali kemenu sebelumnya.

     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/0df873c6-5d0e-4354-90a3-219d9bd4f781)

   - def menu crud tugas(): menampilkan menu crud tugas yang mencakup operasi CRUDS(Create, Read, Update, Delete, Searching) dan pilihan kembali kemenu sebelumnya.
   
     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/b37a06a0-dc39-4800-adc7-944d25a40aba)

   - def menu crud proyek update(): menampilkan menu crud proyek update yang mencakup operasi CRUDS(Create, Read, Update, Delete, Searching) dan pilihan kembali kemenu sebelumnya.

     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/6fb36f0d-78b0-46e4-9c8e-be0a554ff476)

   - def cek email manajer() : digunakan untuk memeriksa apakah seorang manajer dengan alamat email tertentu sudah terdaftar dalam database. Fungsi ini melakukan query ke database untuk mencari manajer 
     dengan alamat email yang diberikan, kemudian mengembalikan True jika manajer tersebut ditemukan dan False jika tidak ditemukan.

     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/43e6fdc0-3b8b-4e33-8407-ab601264b097)

   - def validasi login manajer() : digunakan untuk memvalidasi login manajer berdasarkan email dan password yang diberikan. Fungsi ini melakukan query ke database untuk mencocokkan email dan password dengan 
     entri di tabel manajer. Jika ada hasil yang sesuai, maka fungsi akan mengembalikan nilai True, menandakan bahwa login berhasil. Jika tidak ada hasil yang sesuai, fungsi akan mengembalikan nilai False, 
     menandakan bahwa login gagal.

     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/c7bc95ab-6f47-47ae-8838-5ca4b500b5fc)

   - def ambil nama manajer() : mengambil nama manajer dari database berdasarkan email dan ID manajer yang diberikan. Jika data manajer ditemukan sesuai dengan email dan ID yang diberikan, maka fungsi ini 
     mengembalikan nama manajer. Jika tidak ditemukan, fungsi ini mengembalikan False.

     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/eb02f266-6e9c-4bfc-974d-ad9d26e189ed)

   - def cek_email_karyawan():   digunakan untuk memeriksa apakah seorang karyawan dengan email tertentu sudah terdaftar dalam database karyawan. Fungsi ini melakukan query ke database untuk mencari data 
     karyawan berdasarkan email yang diberikan. Jika email karyawan tersebut ditemukan dalam database, fungsi ini akan mengembalikan nilai True, yang menunjukkan bahwa karyawan tersebut sudah terdaftar. Jika 
     tidak ditemukan, maka fungsi ini akan mengembalikan nilai False.

     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/bb8a5f49-72fb-4ffa-affd-e7c80c760b12)

   - def validasi_login_karyawan(): digunakan untuk melakukan validasi login karyawan dengan memeriksa apakah email dan password yang dimasukkan sesuai dengan data yang ada dalam database. Jika data karyawan
     dengan email dan password yang sesuai ditemukan, fungsi akan mengembalikan True, jika tidak ditemukan, maka akan mengembalikan False.

     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/9e43cb01-127d-4f2b-a615-ad887687665b)

   - def ambil_nama_karyawan(): digunakan untuk mengambil nama karyawan berdasarkan email dan ID karyawan yang diberikan. Fungsi ini menjalankan query SQL untuk mencari entri karyawan yang sesuai dengan
     email dan ID karyawan yang diberikan. Jika ada hasil yang sesuai, maka nama karyawan akan diambil dari hasil query dan dikembalikan. Jika tidak ada hasil yang sesuai, maka fungsi akan mengembalikann 
     nilai False.

     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/eca90a43-9b70-4e5e-9a62-81d67ea26ffc)

   - def menu_login(): digunakan untuk mengelola proses login ke dalam sistem. Saat fungsi ini dijalankan, pengguna akan diminta untuk memilih apakah ingin login sebagai karyawan atau manajer, atau keluar 
     dari aplikasi. Setelah itu, pengguna diminta untuk memasukkan email dan ID (untuk karyawan) atau ID (untuk manajer) mereka. Jika informasi yang dimasukkan valid, pengguna akan berhasil login dan 
     diarahkan ke menu yang sesuai (menu karyawan atau menu manajer). Jika informasi yang dimasukkan tidak valid atau tidak ditemukan, pesan kesalahan akan ditampilkan.

     Penggunaan fungsi menu_login() akan menampilkan tampilan awal aplikasi,
     diikuti dengan proses login ke dalam sistem.

     ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/5e5e6588-f597-4a95-aa20-1b18f79a725e)

###### Manajer
- Pengelolaan Proyek

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/db5681d3-ecb3-4670-9d73-bd521fcf8393)

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/936dfafd-061d-49f9-9864-1d49588fab63)

- Pengelolaan Proyek Update
  
  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/d13292dc-be1f-48df-bef9-2f16d8d8917e)

- Pengelolaan Tugas
  
  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/098c2030-ab83-42cd-8555-42c5b3cb8abc)

- Pengelolaan Karyawan

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/5493cc90-4d0a-41b7-818b-1c1731c659e7)
  
###### Karyawan
- Melihat Tugas
  
  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/35ff8150-a8ea-4f43-82e3-db6900bdf147)

- Pengubahan Status Tugas

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/f83edf0a-67b2-4b06-b784-f111291eecb7)

  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/a15730ad-3f39-465e-a075-0f8cadca5a9a)
  
- Melihat Proyek Update
  
  ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/9852c0b3-c368-4536-aeec-1cd39a9c0b09)

## Cara Penggunaan

**Tampilan Awal Program**
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/1d72c313-dcb9-4ff7-ab3b-a6bde695edd9)
   Ketik "1" untuk login karyawan, ketik "2" untuk login manajer, dan ketik "3" untuk keluar dari program.
   
**Login Karyawan**
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/c293791e-22bc-4f5d-a2bb-2ba8e2a36e24)
   Masukan email dan id karyawan yang sesuai jika sudah klik "enter".
   
1. Tampilan Login Karyawan Berhasil
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/dbe5e28f-61dd-4ff4-84bc-459f42dbf4f7)

2. Lihat Daftar Tugas
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/fd33418c-94b8-4a26-b611-0e41f0554d9f)
   Ketik "1" Untuk Lihat Daftar Tugas
   
3. Edit Status Tugas
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/dbe5e28f-61dd-4ff4-84bc-459f42dbf4f7)
   Ketik "2" Untuk Edit Status Tugas
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/6f744bef-71ab-40bd-b728-d82142707d53)
   Masukan ID Tugas yang ingin diperbarui
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/d19e89c0-7143-4f42-b329-d6ad79d25077)
   Selesaikan perintah dengan mengisi yang sesuai
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/2060fa6f-ed8b-4c9a-9518-f07632ff59cc)
   Tampilan Berhasil
   
4. Cari Tugas
   
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/dbe5e28f-61dd-4ff4-84bc-459f42dbf4f7)
   Ketik "3" Untuk Cari Tugas
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/c308c3d7-e6c7-444f-9029-e40dee29a4c8)
   Menampilkan Daftar Tugas
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/3079160e-2886-4f3d-bac0-777148baee0c)
   Masukan Nama Tugas yang akan dicari
   
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/443d72af-b272-4e90-bf2b-95aef9c86abd)
   Tugas ditemukan
   
5. Urut Tugas
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/0ff0e49f-5243-4b53-acbb-3a2e5bfee949)

6. Lihat Proyek Update
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/76bf8308-35a4-4c4f-ac28-09b5db221bc2)

7. Kembali
   
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/fc3548db-4401-42f0-ae4f-eed2c50906a3)
    
**Login Manajer**

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/89f86c48-31a7-4714-9e8e-5cd7d5996075)
    Masukan email dan id manajer yang sesuai jika sudah klik "enter".
    
1. Tampilan Login Manajer Berhasil

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/fbc4d03c-6631-40c7-ba02-a8c63610a54e)
    Ketik "1" Untuk masuk kemenu kelola proyek, dan ketik "2" untuk Kembali.
    
2. Tampilan Menu Pengelolaan Proyek

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
    
3. Tambah Proyek

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/ba14a11b-2a39-4952-911b-91ac51f30eb2)
    Ketik "1" untuk tambah proyek

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/049eaef1-0158-411c-8187-a75be5c4ae53)
    Masukan data yang sesuai jika sudah klik enter
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/f6dd0d0e-d46a-4f30-a439-bed0b0aefb83)
    Tampilan data berhasil ditambahkan
    
4. Hapus Proyek

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
    Ketik "2" untuk Hapus Proyek

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/0cf9d3bb-976f-4d03-81fe-4c898ecd66f1)
    Masukan ID Proyek yang akan dihapus
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/a79a862e-959b-4c37-a5d3-7b144ae32fc4)
    Tekan Enter untuk melanjutkan
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/81c826de-9f5c-4c59-beee-585ceb848d90)
    Tampilan berhasil menghapus proyek

5. Perbarui Proyek
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
    Ketik "3" untuk Perbarui Proyek
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cfd2484f-d408-45dc-8ee1-3ef2ff06c771)
    Masukan ID Proyek yang akan diperbarui, dan selesaikan
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/51b68756-f03e-4402-a7f2-0fe932713db4)
    Tampilan berhasil memperbarui proyek

6. Cari Proyek

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
    Ketik "4" untuk Cari Proyek
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/becc4a14-a8fa-4349-baeb-e1ee9dd0508e)
    Tampilan Proyek Ditemukan

7. Urutkan Proyek

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
    Ketik "5" untuk Urutkan Proyek
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/10831cb5-a623-4d11-8770-05fcb90c4d9d)
    Tampilan diurutkan berdasarkan anggaran


8. Tampilkan Semua Proyek
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
    Ketik "6" untuk Menampilkan Semua Proyek
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/d3c6a0f6-9d13-46e7-9f40-320454b42c03)
    Tampilan Semua Proyek

9. Kembali

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
    Ketik "9" untuk kembali ke Menu sebelumnya

10. Kelola tugas

    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
    Ketik "7" untuk Kelola Tugas
    
    1. Menu Pengelolaan Tugas

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/48be95f1-560a-4dcb-982f-c8394aeafc67)

    2. Tambah Tugas

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/f813874a-5c63-4ff0-9849-48589293022e)
       Ketik "1" untuk Menambahkan Tugas
       
       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/2d6be4f0-10c7-4461-8bea-8686f461b2c4)
       Tampilan Tugas Berhasil diTambahkan

    3. Hapus Tugas

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/48be95f1-560a-4dcb-982f-c8394aeafc67)
       Ketik "2" untuk Menghapus Tugas

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/477e4883-69b2-4339-b703-2cecdbdab6c8)
       Masukkan ID Tugas yang akan dihapus
       
       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/b1792dd1-ee2b-4650-9bd4-aae6e0d582f0)
       Tampilan Berhasil Menghapus Tugas

    4. Perbarui Tugas

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/48be95f1-560a-4dcb-982f-c8394aeafc67)
       Ketik "3" untuk Memperbarui Tugas
       
       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/0242cf6b-e209-47f2-bd5e-d88808e3fa07)
       Masukan ID Tugas yang akan diperbarui, dan selesaikan perintahnya
       
       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/dc258b61-21d8-47ce-b64e-423551aa55d4)
       Tampilan Tugas Berhasil diPerbarui

    5. Cari Tugas

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/9b6eb613-d8d8-4f61-b3d5-27ce2450218e)
       Ketik "4" untuk cari tugas, setelah itu masukan Nama Tugas yang akan dicari, Dan Tugas Ditemukan

    6. Urutkan Tugas
 
        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/48be95f1-560a-4dcb-982f-c8394aeafc67)
        Ketik "5" untuk mengurutkan Tugas
       
        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/7ddb564f-17a6-48d1-8db0-a3c2c307d2ca)
        Tampilkan Berhasil Mengurutkan Tugas Berdasarkan Tenggat Tugas
       

    7. Tampilkan Semua Tugas
 
        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/48be95f1-560a-4dcb-982f-c8394aeafc67)
        Ketik "6" untuk Menampilkan Semua Tugas
 
        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/75a9164a-8855-4fbd-b196-097437a87f06)
        Tampilan Semua Tugas
 
    8. Kembali

        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/48be95f1-560a-4dcb-982f-c8394aeafc67)
        Ketik "7" untuk kembali ke menu sebelumnya

11. Kelola Proyek Update
    
    ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
    Ketik "8" untuk Kelola Proyek Update
    
    1. Menu Pengelolaan Proyek Update

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/8c49c745-5215-4650-a716-49c01f05dbf6)
       
    2. Tambah Proyek Update

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/19c5804b-3dc8-4566-a379-781517589058)
       Ketik "1" untuk Menambahkan Proyek Update
       
       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/a33cfdd5-d01c-4c0a-9bad-ade49f423dfd)
       Tampilan Berhasil diTambahkan

    3. Hapus Proyek Update

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
       Ketik "2" untuk Menghapus Proyek Update

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/54ee38c3-9d85-450c-95ce-977669c5ecce)
       Tampilan Sebelum dihapus

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/4a3f63de-971b-4663-9060-4c498dbc74ab)
       Masukan ID Proyek update yang akan dihapus

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/0cfef2e7-8a3c-4f24-b45c-a07b19e062d1)
       Tampilan Setelah Dihapus

    4. Perbarui Proyek Update

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/25869b88-4356-4924-b370-2cffe2e15290)
       Ketik "3" untuk Memperbarui Proyek Update, setelah itu selesaikan perintahnya, dan Proyek Update berhasil diperbarui
       
       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/428e11a6-67c8-4e8c-9b79-00684e092084)
       Tampilan Setelah Diperbarui

    5. Cari Proyek Update

       ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/394f1bc6-5bef-4afc-8c2c-ededc495f45d)
       Ketik "4" untuk cari proyek update, setelah itu masukkan Nama Proyek Update yang akan dicari, dan Proyek Update Ditemukan

    6. Urutkan Proyek Update

        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
       Ketik "5" untuk Mengurutkan Proyek Update

        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/371d645d-fc8d-4526-8037-c4848f5086ed)
       Tampilan Berhasil Mengurutkan Tugas Berdasarkan Tanggal

    7. Tampilkan Semua Proyek Update
 
        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
        Ketik "6" untuk Menampilkan Semua Proyek Update

        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/8d8b2796-511b-4fac-a3be-04f233a7f618)
        Tampilan Semua Proyek Update

    8. Kembali
  
        ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/cbf799bc-fc50-4711-8f0f-049a53beefff)
        Ketik "7" untuk Kembali kemenu Sebelumnya


**Keluar**

   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/38cd5693-fe10-49d5-ac8f-b4a33798c335)
    Ketik "3" untuk keluar
    
   ![image](https://github.com/PA-A23-KELOMPOK-6/PA-A23-KELOMPOK-6/assets/144349308/64824a1f-f482-4d25-a484-5cd4f3bb1250)
    Menampilkan Anda telah keluar dari aplikasi





   
   




   
