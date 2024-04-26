import mysql.connector
import math
from prettytable import PrettyTable

# Koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="manajemen_proyek_perusahaan"
)
cursor=mydb.cursor()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def tambah_di_akhir(self, pesanan):
        new_node = Node(pesanan)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def cari_pengguna(self, id, email):
        current_node = self.head
        while current_node is not None:
            pengguna_id, pengguna_nama, pengguna_email = current_node.data
            if pengguna_id == id or pengguna_email == email:
                return current_node.data
            current_node = current_node.next
        return None
        
    def cari_proyek(self, id_proyek):
        current_node = self.head
        while current_node is not None:
            if current_node.data[0] == id_proyek:
                return current_node.data
            current_node = current_node.next
        return None
    
    def cari_tugas(self, id_tugas):
        current_node = self.head
        while current_node is not None:
            if current_node.data[0] == id_tugas:
                return current_node.data
            current_node = current_node.next
        return None
    
    def cari_proyek_update(self, id_proyek_update):
        current_node = self.head
        while current_node is not None:
            if current_node.data[0] == id_proyek_update:
                return current_node.data
            current_node = current_node.next
        return None
    
    def ubah_ke_array(self):
        arr = []
        current_node = self.head
        while current_node:
            arr.append(current_node.data)
            current_node = current_node.next
        return arr
        
    def jump_search_proyek(self, arr, nama):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while arr[min(step, n) - 1][2].lower() < nama.lower():
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        while arr[prev][2].lower() < nama.lower():
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev][2].lower() == nama.lower():
            return prev
        return -1
    
    def jump_search_tugas(self, arr, nama):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while arr[min(step, n) - 1][1].lower() < nama.lower():
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        while arr[prev][1].lower() < nama.lower():
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev][1].lower() == nama.lower():
            return prev
        return -1
    
    def jump_search_proyek_update(self, arr, nama):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while arr[min(step, n) - 1][2].lower() < nama.lower():
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        while arr[prev][2].lower() < nama.lower():
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev][2].lower() == nama.lower():
            return prev
        return -1

    def cari_proyek_linked_list(self, nama):
        arr = self.ubah_ke_array()
        index = self.jump_search_proyek(arr, nama)
        if index != -1:
            print("+=================================================+")
            print("|                Proyek ditemukan!                |")
            print("+=================================================+")
            table = PrettyTable()
            table.field_names = ["ID Proyek", "Deskripsi", "Nama Proyek", "Anggaran", "Status", "ID Manajer", "Tanggal Mulai", "Tanggal Selesai"]
            table.add_row(arr[index])
            print(table)
        else:
            print("+=================================================+")
            print("|             Proyek tidak ditemukan.             |")
            print("+=================================================+")
            return None

    def cari_tugas_linked_list(self, nama):
        arr = self.ubah_ke_array()
        index = self.jump_search_tugas(arr, nama)
        if index != -1:
            print("+=================================================+")
            print("|                  Tugas ditemukan!               |")
            print("+=================================================+")
            table = PrettyTable()
            table.field_names = ["ID Tugas", "Nama", "Deskripsi", "Status", "Tenggat", "ID Karyawan"]
            table.add_row(arr[index])
            print(table)
        else:
            print("+=================================================+")
            print("|              Tugas tidak ditemukan.             |")
            print("+=================================================+")
            return None
    
    def cari_proyek_update_linked_list(self, nama):
        arr = self.ubah_ke_array()
        index = self.jump_search_proyek_update(arr, nama)
        if index != -1:
            print("+=================================================+")
            print("|                Proyek Update ditemukan!         |")
            print("+=================================================+")
            table = PrettyTable()
            table.field_names = ["ID Update", "nama", "deskripsi", "tanggal update", "ID Proyek"]
            table.add_row(arr[index])
            print(table)
        else:
            print("+=================================================+")
            print("|             Proyek Update tidak ditemukan.      |")
            print("+=================================================+")
            return None

    def tampilkan_semua_proyek(self):
        table = PrettyTable()
        table.field_names = ["ID Proyek", "Deskripsi", "Nama Proyek", "Anggaran", "Status", "ID Manajer","Tanggal Mulai", "Tanggal Selesai"]
        current_node = self.head
        while current_node is not None:
            if len(current_node.data) == 8: 
                table.add_row(current_node.data)
            else:
                print("+=================================================+")
                print(" Data proyek tidak lengkap:", current_node.data     )
                print("+=================================================+")
            current_node = current_node.next
        print(table)
        
    def tampilkan_semua_tugas(self):
        table = PrettyTable()
        table.field_names = ["ID Tugas", "Nama", "Deskripsi", "Status", "Tenggat", "ID Karyawan"]
        current_node = self.head
        while current_node is not None:
            if len(current_node.data) == 6: 
                table.add_row(current_node.data)
            else:
                print("+=================================================+")
                print(" Data tugas tidak lengkap:", current_node.data     )
                print("+=================================================+")
            current_node = current_node.next
        print(table)
    
    def tampilkan_proyek_update(self):
        table = PrettyTable()
        table.field_names = ["ID Update", "Nama", "Deskripsi", "tanggal update", "ID Proyek"]
        current_node = self.head
        while current_node is not None:
            if len(current_node.data) == 5: 
                table.add_row(current_node.data)
            else:
                print("+=================================================+")
                print(" Data Proyek Update tidak lengkap:", current_node.data     )
                print("+=================================================+")
            current_node = current_node.next
        print(table)
        
    def tambah_proyek(self, id_proyek, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai):
        cursor = mydb.cursor()
        query = "INSERT INTO proyek (ID_proyek, deskripsi, nama, anggaran, status, ID_manajer, tanggal_mulai, tanggal_selesai) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (id_proyek, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai)
        cursor.execute(query, values)
        mydb.commit()
        cursor.close()
        self.tambah_di_akhir((id_proyek, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai))
        print("+=================================================+")
        print("|          Proyek berhasil ditambahkan.           |")
        print("+=================================================+")
        
    def tambah_tugas(self, id_tugas, nama, deskripsi, status, tenggat, id_karyawan):
        cursor = mydb.cursor()
        query = "INSERT INTO tugas (ID_tugas, nama, deskripsi, status, tenggat, ID_karyawan) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id_tugas, nama, deskripsi, status, tenggat, id_karyawan)
        cursor.execute(query, values)
        mydb.commit()
        cursor.close()
        self.tambah_di_akhir((id_tugas, nama, deskripsi, status, tenggat, id_karyawan))
        print("+=================================================+")
        print("|           Tugas berhasil ditambahkan.           |")
        print("+=================================================+")

    def tambah_proyek_update(self, id_proyek_update, nama, deskripsi, tanggal_update, id_proyek):
        cursor = mydb.cursor()
        query = "INSERT INTO proyek_update (ID_update, nama, deskripsi, tanggal_update, ID_proyek) VALUES (%s, %s, %s, %s, %s)"
        values = (id_proyek_update, nama, deskripsi, tanggal_update, id_proyek)
        cursor.execute(query, values)
        mydb.commit()
        cursor.close()
        self.tambah_di_akhir((id_proyek_update, nama, deskripsi, tanggal_update, id_proyek))
        print("+=================================================+")
        print("|          Proyek Update berhasil ditambahkan.    |")
        print("+=================================================+")
        
    def hapus_proyek(self, id_proyek):
        cursor = mydb.cursor()
        query = "DELETE FROM proyek WHERE ID_proyek = %s"
        cursor.execute(query, (id_proyek,))
        mydb.commit()
        cursor.close()
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.data[0] == id_proyek:
                if prev_node is None:
                    self.head = current_node.next
                else:
                    prev_node.next = current_node.next
                print("+=================================================+")
                print("|            Proyek berhasil dihapus.             |")
                print("+=================================================+")
                return
            prev_node = current_node
            current_node = current_node.next
        print("+=================================================+")
        print("|             Proyek tidak ditemukan.             |")
        print("+=================================================+")
        
    def hapus_tugas(self, id_tugas):
        cursor = mydb.cursor()
        query = "DELETE FROM tugas WHERE ID_tugas = %s"
        cursor.execute(query, (id_tugas,))
        mydb.commit()
        cursor.close()
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.data[0] == id_tugas:
                if prev_node is None:
                    self.head = current_node.next
                else:
                    prev_node.next = current_node.next
                print("+=================================================+")
                print("|            Tugas berhasil dihapus.              |")
                print("+=================================================+")
                return
            prev_node = current_node
            current_node = current_node.next
        print("+=================================================+")
        print("|              Tugas tidak ditemukan.             |")
        print("+=================================================+")

    def hapus_proyek_update(self, id_proyek_update):
        cursor = mydb.cursor()
        query = "DELETE FROM proyek_update WHERE ID_update = %s"
        cursor.execute(query, (id_proyek_update,))
        mydb.commit()
        cursor.close()
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.data[0] == id_proyek_update:
                if prev_node is None:
                    self.head = current_node.next
                else:
                    prev_node.next = current_node.next
                print("+=================================================+")
                print("|            Proyek Update berhasil dihapus.      |")
                print("+=================================================+")
                return
            prev_node = current_node
            current_node = current_node.next
        print("+=================================================+")
        print("|             Proyek Update tidak ditemukan.      |")
        print("+=================================================+")
        

    def perbarui_tugas(self, id_tugas, nama, deskripsi, status, tenggat, id_karyawan):
        tugas = self.cari_tugas(id_tugas)
        cursor = mydb.cursor()
        query = "UPDATE tugas SET nama = %s, deskripsi = %s, status = %s, tenggat = %s, ID_karyawan = %s WHERE ID_tugas = %s"
        values = (nama, deskripsi, status, tenggat, id_karyawan, id_tugas)
        cursor.execute(query, values)
        mydb.commit()
        cursor.close()
        
        current_node = self.head
        while current_node is not None:
            if current_node.data[0] == id_tugas:
                current_node.data = (id_tugas, nama, deskripsi, status, tenggat, id_karyawan)
                print("+=================================================+")
                print("|            Tugas berhasil diperbarui.           |")
                print("+=================================================+")
                return
            current_node = current_node.next

    def perbarui_proyek(self, id_proyek, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai):
        proyek = self.cari_proyek(id_proyek)
        cursor = mydb.cursor()
        query = "UPDATE proyek SET deskripsi = %s, nama = %s, anggaran = %s, status = %s, ID_manajer = %s, tanggal_mulai = %s, tanggal_selesai = %s WHERE ID_proyek = %s"
        values = (deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai, id_proyek)
        cursor.execute(query, values)
        mydb.commit()
        cursor.close()

        current_node = self.head
        while current_node is not None:
            if current_node.data == id_proyek:
                current_node.data = (id_proyek, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai)
                print("+=================================================+")
                print("|           Proyek berhasil diperbarui.           |")
                print("+=================================================+")
                return
            current_node = current_node.next

    def perbarui_proyek_update(self, id_proyek_update, nama, deskripsi, tanggal_update, id_proyek):
        proyek_update = self.cari_proyek_update(id_proyek_update)
        cursor = mydb.cursor()
        query = "UPDATE proyek_update SET nama = %s, deskripsi = %s, tanggal_update = %s, ID_proyek = %s WHERE ID_update = %s"
        values = (nama, deskripsi, tanggal_update, id_proyek, id_proyek_update)
        cursor.execute(query, values)
        mydb.commit()
        cursor.close()

        current_node = self.head
        while current_node is not None:
            if current_node.data == id_proyek_update:
                current_node.data = (id_proyek_update, nama, deskripsi, tanggal_update, id_proyek)
                print("+=================================================+")
                print("|           Proyek Update berhasil diperbarui.    |")
                print("+=================================================+")
                return
            current_node = current_node.next
            
def menu_karyawan():

    linked_list_tugas = LinkedList()  
    cursor = mydb.cursor()
    query = "SELECT * FROM tugas"
    cursor.execute(query)
    tugas_records = cursor.fetchall()
    for record in tugas_records:
        linked_list_tugas.tambah_di_akhir(record)
    cursor.close()

    linked_list_proyek_update = LinkedList()  
    cursor = mydb.cursor()
    query = "SELECT * FROM proyek_update"
    cursor.execute(query)
    proyek_update_records = cursor.fetchall()
    for record in proyek_update_records:
        linked_list_proyek_update.tambah_di_akhir(record)
    cursor.close()

    while True:
        print("\n")
        print("+=================================================+")
        print("|            Menu Karyawan                        |")
        print("+=================================================+")
        print("|       1. Lihat Daftar Tugas                     |")
        print("|       2. Edit Status Tugas                      |")
        print("|       3. Cari Tugas                             |")
        print("|       4. Urut Tugas                             |")
        print("|       5. Lihat Proyek Update                    |")
        print("|       6. Kembali                                |")
        print("+=================================================+")
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")
        if pilihan == "1":
            linked_list_tugas.tampilkan_semua_tugas()
        elif pilihan == "2":
            id_tugas = input("Masukkan ID Tugas yang akan diperbarui: ")
            nama = input("Masukkan Nama Tugas: ")
            deskripsi = input("Masukkan Deskripsi Tugas: ")
            status = input("Masukkan Status Tugas: ")          
            tenggat = input("Masukkan Tenggat Tugas (YYYY-MM-DD): ")
            id_karyawan = input("Masukkan ID Karyawan Pelaksana: ")
            linked_list_tugas.perbarui_tugas(id_tugas, nama, deskripsi, status, tenggat, id_karyawan)
        elif pilihan == "3":
            nama_tugas = input("Masukkan Nama Tugas yang akan dicari: ")
            linked_list_tugas.cari_tugas_linked_list(nama_tugas)
        elif pilihan == "4":  #blom
            print('belom')
        elif pilihan == "5":
            menu_crud_proyek_update()
        elif pilihan == "6":
            menu_login()
            break
        else:
            print("+=================================================+")
            print("| Pilihan tidak valid. Silakan masukkan angka 1-6.|")
            print("+=================================================+")

def menu_manajer():
    while True:
        print("\n")
        print("+=================================================+")
        print("|            Menu Manajer                         |")
        print("+=================================================+")
        print("|       1. CRUD Proyek                            |")
        print("|       2. CRUD Tugas                             |")
        print("|       3. CRUD Proyek Update                     |")
        print("|       4. Kembali                                |")
        print("+=================================================+")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            menu_crud_proyek()
        elif pilihan == "2":
            menu_crud_tugas()
        elif pilihan == "3":
            menu_crud_proyek_update()
        elif pilihan == "4":
            menu_login()
            break
        else:
            print("+=================================================+")
            print("| Pilihan tidak valid. Silakan masukkan angka 1-3.|")
            print("+=================================================+")

def menu_crud_proyek():
    linked_list_proyek = LinkedList()  
    cursor = mydb.cursor()
    query = "SELECT * FROM proyek"
    cursor.execute(query)
    proyek_records = cursor.fetchall()
    for record in proyek_records:
        linked_list_proyek.tambah_di_akhir(record)
    cursor.close()
    
    while True:
        print("\n")
        print("+=================================================+")
        print("|                  Menu CRUD Proyek               |")
        print("+=================================================+")
        print("|       1. Tambah Proyek                          |")
        print("|       2. Hapus Proyek                           |")
        print("|       3. Perbarui Proyek                        |")
        print("|       4. Cari Proyek                            |")
        print("|       5. Tampilkan Semua Proyek                 |")
        print("|       6. Kembali                                |")
        print("+=================================================+")
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")
        
        if pilihan == "1":
            id_proyek = input("Masukkan ID Proyek: ")
            nama = input("Masukkan Nama Proyek: ")
            deskripsi = input("Masukkan Deskripsi Proyek: ")
            anggaran = input("Masukkan Anggaran Proyek: ")
            status = input("Masukkan Status Proyek: ")
            id_manajer = input("Masukkan ID Manajer Proyek: ")
            tanggal_mulai = input("Masukkan Tanggal Mulai Proyek (YYYY-MM-DD): ")
            tanggal_selesai = input("Masukkan Tanggal Selesai Proyek (YYYY-MM-DD): ")
            linked_list_proyek.tambah_proyek(id_proyek, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai)
        elif pilihan == "2":
            id_proyek = input("Masukkan ID Proyek yang akan dihapus: ")
            linked_list_proyek.hapus_proyek(id_proyek)
        elif pilihan == "3":
            id_proyek = input("Masukkan ID Proyek yang akan diperbarui: ")
            nama = input("Masukkan Nama Proyek: ")
            deskripsi = input("Masukkan Deskripsi Proyek: ")
            anggaran = input("Masukkan Anggaran Proyek: ")
            status = input("Masukkan Status Proyek: ")
            id_manajer = input("Masukkan ID Manajer Proyek: ")
            tanggal_mulai = input("Masukkan Tanggal Mulai Proyek (YYYY-MM-DD): ")
            tanggal_selesai = input("Masukkan Tanggal Selesai Proyek (YYYY-MM-DD): ")
            linked_list_proyek.perbarui_proyek(id_proyek, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai)
        elif pilihan == "4":
            nama_proyek = input("Masukkan Nama Proyek yang akan dicari: ")
            linked_list_proyek.cari_proyek_linked_list(nama_proyek)
        elif pilihan == "5":
            linked_list_proyek.tampilkan_semua_proyek()
        elif pilihan == "6":
            menu_manajer()
            break
        else:
            print("+=================================================+")
            print("| Pilihan tidak valid. Silakan masukkan angka 1-6.|")
            print("+=================================================+")

def menu_crud_tugas():
    linked_list_tugas = LinkedList()  
    
    cursor = mydb.cursor()
    query = "SELECT * FROM tugas"
    cursor.execute(query)
    tugas_records = cursor.fetchall()
    for record in tugas_records:
        linked_list_tugas.tambah_di_akhir(record)
    cursor.close()
    
    while True:
        print("\n")
        print("+=================================================+")
        print("|                  Menu CRUD Tugas                |")
        print("+=================================================+")
        print("|       1. Tambah Tugas                           |")
        print("|       2. Hapus Tugas                            |")
        print("|       3. Perbarui Tugas                         |")
        print("|       4. Cari Tugas                             |")
        print("|       5. Tampilkan Semua Tugas                  |")
        print("|       6. Kembali                                |")
        print("+=================================================+")
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")
        
        if pilihan == "1":
            id_tugas = input("Masukkan ID Tugas: ")
            nama = input("Masukkan Nama Tugas: ")
            deskripsi = input("Masukkan Deskripsi Tugas: ")
            status = input("Masukkan Status Tugas: ")
            tenggat = input("Masukkan Tenggat Tugas (YYYY-MM-DD): ")
            id_karyawan = input("Masukkan ID Karyawan Pelaksana: ")
            linked_list_tugas.tambah_tugas(id_tugas, nama, deskripsi, status, tenggat, id_karyawan)
        elif pilihan == "2":
            id_tugas = input("Masukkan ID Tugas yang akan dihapus: ")
            linked_list_tugas.hapus_tugas(id_tugas)
        elif pilihan == "3":
            id_tugas = input("Masukkan ID Tugas yang akan diperbarui: ")
            nama = input("Masukkan Nama Tugas: ")
            deskripsi = input("Masukkan Deskripsi Tugas: ")
            status = input("Masukkan Status Tugas: ")
            tenggat = input("Masukkan Tenggat Tugas (YYYY-MM-DD): ")
            id_karyawan = input("Masukkan ID Karyawan Pelaksana: ")
            linked_list_tugas.perbarui_tugas(id_tugas, nama, deskripsi, status, tenggat, id_karyawan)
        elif pilihan == "4":
            nama_tugas = input("Masukkan Nama Tugas yang akan dicari: ")
            linked_list_tugas.cari_tugas_linked_list(nama_tugas)
        elif pilihan == "5":
            linked_list_tugas.tampilkan_semua_tugas()
        elif pilihan == "6":
            menu_manajer()
            break
        else:
            print("+=================================================+")
            print("| Pilihan tidak valid. Silakan masukkan angka 1-6.|")
            print("+=================================================+")

def cek_email_manajer(email_manajer):
    query = "SELECT * from manajer where email = %s"
    cursor.execute(query, (email_manajer,))
    hasil = cursor.fetchone()
    if hasil : 
        return True
    else :
        return False
    
def validasi_login_manajer(email_manajer, pw):
    query = "SELECT * from manajer where email = %s AND ID_manajer = %s"
    cursor.execute(query, (email_manajer, pw))
    hasil = cursor.fetchone()
    if hasil : 
        return True
    else :
        return False
    
def ambil_nama_manajer(email_manajer, pw) :
    query = "SELECT * from manajer where email = %s AND ID_manajer = %s"
    cursor.execute(query, (email_manajer, pw))
    hasil = cursor.fetchone()
    if hasil : 
        nama = str(hasil[1])
        return nama
    else :
        return False


def cek_email_karyawan(email_karyawan):
    query = "SELECT * from karyawan where email = %s"
    cursor.execute(query, (email_karyawan,))
    hasil = cursor.fetchone()
    if hasil : 
        return True
    else :
        return False
    
def validasi_login_karyawan(email_karyawan, pw):
    query = "SELECT * from karyawan where email = %s AND ID_karyawan = %s"
    cursor.execute(query, (email_karyawan, pw))
    hasil = cursor.fetchone()
    if hasil : 
        return True
    else :
        return False
    
def ambil_nama_karyawan(email_karyawan, pw) :
    query = "SELECT * from karyawan where email = %s AND ID_karyawan = %s"
    cursor.execute(query, (email_karyawan, pw))
    hasil = cursor.fetchone()
    if hasil : 
        nama = str(hasil[1])
        return nama
    else :
        return False


def menu_crud_proyek_update():
    linked_list_proyek_update = LinkedList()  
    cursor = mydb.cursor()
    query = "SELECT * FROM proyek_update"
    cursor.execute(query)
    proyek_update_records = cursor.fetchall()
    for record in proyek_update_records:
        linked_list_proyek_update.tambah_di_akhir(record)
    cursor.close()
    
    while True:
        print("\n")
        print("+=================================================+")
        print("|                  Menu CRUD Proyek update        |")
        print("+=================================================+")
        print("|       1. Tambah proyek update                   |")
        print("|       2. Hapus proyek update                    |")
        print("|       3. Perbarui proyek update                 |")
        print("|       4. Cari proyek update                     |")
        print("|       5. Tampilkan Semua proyek update          |")
        print("|       6. Kembali                                |")
        print("+=================================================+")
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")
        if pilihan == "1":
            id_proyek_update = input("Masukkan ID proyek update: ")
            nama = input("Masukkan Nama proyek update: ")
            deskripsi = input("Masukkan Deskripsi Proyek: ")
            tanggal_update = input("Masukkan tanggal update (YYYY-MM-DD): ")
            id_proyek = input("Masukkan Id proyek: ")
            linked_list_proyek_update.tambah_proyek_update(id_proyek_update, nama, deskripsi, tanggal_update, id_proyek)
        elif pilihan == "2":
            id_proyek_update = input("Masukkan ID proyek update yang akan dihapus: ")
            linked_list_proyek_update.hapus_proyek_update(id_proyek_update)
        elif pilihan == "3":
            id_proyek_update = input("Masukkan ID proyek update: ")
            nama = input("Masukkan Nama proyek update: ")
            deskripsi = input("Masukkan Deskripsi Proyek: ")
            tanggal_update = input("Masukkan tanggal update (YYYY-MM-DD): ")
            id_proyek = input("Masukkan Id proyek: ")
            linked_list_proyek_update.perbarui_proyek_update(id_proyek_update, nama, deskripsi, tanggal_update, id_proyek)
        elif pilihan == "4":
            nama_proyek_update = input("Masukkan Nama proyek update yang akan dicari: ")
            linked_list_proyek_update.cari_proyek_update_linked_list(nama_proyek_update)
        elif pilihan == "5":
            linked_list_proyek_update.tampilkan_proyek_update()
        elif pilihan == "6":
            menu_manajer()
            break
        else:
            print("+=================================================+")
            print("| Pilihan tidak valid. Silakan masukkan angka 1-6.|")
            print("+=================================================+")

def menu_login():
    linked_list = LinkedList()
    
    cursor = mydb.cursor()
    query = "SELECT ID_karyawan, nama, email FROM karyawan UNION SELECT ID_manajer, nama, email FROM manajer"
    cursor.execute(query)
    semua_records = cursor.fetchall()
    for record in semua_records:
        linked_list.tambah_di_akhir(record)
    cursor.close()

    while True:
        print("+=================================================+")
        print("|                    Menu Login                   |")
        print("+=================================================+")
        print("|           1. Login sebagai Karyawan             |")
        print("|           2. Login sebagai Manajer              |")
        print("|           3. Keluar                             |")
        print("+=================================================+")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            email_karyawan = input("Masukkan Email Karyawan: ")
            if cek_email_karyawan(email_karyawan) :
                pw = int(input("Masukkan ID Karyawan: "))
                if validasi_login_karyawan(email_karyawan, pw):
                    print("\n")
                    print("+=================================================+")
                    print(f" Login berhasil! Selamat datang, {ambil_nama_karyawan(email_karyawan, pw)}  ")
                    print("+=================================================+")
                    print("\n")
                    menu_karyawan()
                    break
                else:
                    print("+=================================================+")
                    print("|  ID atau email salah atau Anda bukan karyawan.  |")
                    print("+=================================================+")
        elif pilihan == "2":
            email_manajer = input("Masukkan Email Manajer: ")
            if cek_email_manajer(email_manajer) :
                pw = int(input("Masukkan ID Karyawan: "))
                if validasi_login_manajer(email_manajer, pw):
                    print("\n")
                    print("+=================================================+")
                    print("                --- Login berhasil! ---            ")
                    print(f"                Selamat datang, {ambil_nama_manajer(email_manajer, pw)}    ")
                    print("+=================================================+")
                    menu_manajer()  
                    break  
                else:
                    print("+=================================================+")
                    print("|   ID atau email salah atau Anda bukan manajer.  |")
                    print("+=================================================+")
        elif pilihan == "3":
            print("+=================================================+")
            print("|        Anda telah keluar dari aplikasi          |")
            print("+=================================================+")
            break
        else:
            print("+=================================================+")
            print("|  Pilihan tidak valid. Silakan masukkan 1/2/3.   |")
            print("+=================================================+")

print('''
+========================================================================================================+
|                                          +        Aplikasi         +                                   |
|                                       Sistem Manajemen Proyek Perusahaan                               |
+========================================================================================================+
''')
menu_login()