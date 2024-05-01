import mysql.connector
import math
from prettytable import PrettyTable
from datetime import datetime
import os

try:

    mydb = mysql.connector.connect(
        host="db4free.net",
        user="tes123",
        password="123123123",
        database="manajemen_proyek"
    )
        
except mysql.connector.Error as error:
    print("Gagal terhubung ke database: {}".format(error))
        
cursor=mydb.cursor()
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
        
    def jump_search(self, target, key_function):
        try:
            current = self.head
            n = 0
            while current:
                n += 1
                current = current.next
                
            current = self.head
            step = int(math.sqrt(n))
            prev = 0
            while key_function(current.data) < target:
                prev = step
                step += int(math.sqrt(n))
                if prev >= n:
                    return -1, n
                while prev < min(step, n) and key_function(current.data) < target:
                    prev += 1
                    current = current.next
            while key_function(current.data) < target:
                current = current.next
                if current is None:
                    return -1, n
            if key_function(current.data) == target:
                return current.data, n
            return None, n
        except Exception as e:
            print("Error:", e)
            return None, n
            
            
    def cari_proyek(self, nama):
        try:
            key_function = lambda x: x[2].lower() 
            current = self.head
            sorted_head = None
            while current:
                next_node = current.next
                if sorted_head is None or key_function(current.data) < key_function(sorted_head.data):
                    current.next = sorted_head
                    sorted_head = current
                else:
                    temp = sorted_head
                    while temp.next and key_function(current.data) > key_function(temp.next.data):
                        temp = temp.next
                    current.next = temp.next
                    temp.next = current
                current = next_node
                        
            target = nama.lower()
            current = sorted_head
            while current:
                if key_function(current.data) == target:
                    print("+=================================================+")
                    print("|                Proyek ditemukan!                |")
                    print("+=================================================+")
                    table = PrettyTable()
                    table.field_names = ["ID Proyek", "Deskripsi", "Nama Proyek", "Anggaran", "Status", "ID Manajer", "Tanggal Mulai", "Tanggal Selesai"]
                    table.add_row(current.data)
                    print(table)
                    return
                current = current.next
            print("+=================================================+")
            print("|             Proyek tidak ditemukan.             |")
            print("+=================================================+")
        except Exception as e:
            print("Terjadi kesalahan saat mencari proyek:", e)
            
            
    def cari_tugas(self, nama):
        try:
            key_function = lambda x: x[1].lower()
            current = self.head
            sorted_head = None
            while current:
                next_node = current.next
                if sorted_head is None or key_function(current.data) < key_function(sorted_head.data):
                    current.next = sorted_head
                    sorted_head = current
                else:
                    temp = sorted_head
                    while temp.next and key_function(current.data) > key_function(temp.next.data):
                        temp = temp.next
                    current.next = temp.next
                    temp.next = current
                current = next_node
                    
            target = nama.lower()
            current = sorted_head
            while current:
                if key_function(current.data) == target:
                    print("+=================================================+")
                    print("|                  Tugas ditemukan!               |")
                    print("+=================================================+")
                    table = PrettyTable()
                    table.field_names = ["ID Tugas", "Nama", "Deskripsi", "Status", "Tenggat", "ID_Proyek"]
                    table.add_row(current.data)
                    print(table)
                    return
                current = current.next
            print("+=================================================+")
            print("|              Tugas tidak ditemukan.             |")
            print("+=================================================+")
        except Exception as e:
            print("Terjadi kesalahan saat mencari tugas:", e)
            
            
    def cari_proyek_update(self, deskripsi):
        try:
            key_function = lambda x: x[1].lower() 
            current = self.head
            sorted_head = None
            while current:
                next_node = current.next
                if sorted_head is None or key_function(current.data) < key_function(sorted_head.data):
                    current.next = sorted_head
                    sorted_head = current
                else:
                    temp = sorted_head
                    while temp.next and key_function(current.data) > key_function(temp.next.data):
                        temp = temp.next
                    current.next = temp.next
                    temp.next = current
                current = next_node
                    
            target = deskripsi.lower()
            current = sorted_head
            while current:
                if key_function(current.data) == target:
                    print("+=================================================+")
                    print("|                Proyek Update ditemukan!         |")
                    print("+=================================================+")
                    table = PrettyTable()
                    table.field_names = ["ID Update", "Deskripsi", "Tanggal Update", "ID Proyek"]
                    table.add_row(current.data)
                    print(table)
                    return
                current = current.next
            print("+=================================================+")
            print("|             Proyek Update tidak ditemukan.      |")
            print("+=================================================+")
        except Exception as e:
            print("Terjadi kesalahan saat mencari proyek update:", e)
            
            
    def tampilkan_semua_proyek(self):
        table = PrettyTable()
        table.field_names = ["ID Proyek", "Deskripsi", "Nama Proyek", "Anggaran", "Status", "ID Manajer", "Tanggal Mulai", "Tanggal Selesai"]
        current_node = self.head
        try:
            while current_node is not None:
                if len(current_node.data) == 8: 
                    table.add_row(current_node.data)
                else:
                    raise ValueError("Data proyek tidak lengkap: {}".format(current_node.data))
                current_node = current_node.next
            print(table)
        except Exception as e:
            print("+=================================================+")
            print("Error:", str(e))
            print("+=================================================+")
            
            
    def tampilkan_semua_tugas(self):
        table = PrettyTable()
        table.field_names = ["ID Tugas", "Nama", "Deskripsi", "Status", "Tenggat", "ID_Proyek"]
        current_node = self.head
        try:
            while current_node is not None:
                if len(current_node.data) == 6: 
                    table.add_row(current_node.data)
                else:
                    raise ValueError("Data tugas tidak lengkap: {}".format(current_node.data))
                current_node = current_node.next
            print(table)
        except Exception as e:
            print("+=================================================+")
            print("Error:", str(e))
            print("+=================================================+")
            
            
    def tampilkan_proyek_update(self):
        table = PrettyTable()
        table.field_names = ["ID Update", "Deskripsi", "tanggal update", "ID Proyek"]
        current_node = self.head
        try:
            while current_node is not None:
                if len(current_node.data) == 4: 
                    table.add_row(current_node.data)
                else:
                    raise ValueError("Data Proyek Update tidak lengkap: {}".format(current_node.data))
                current_node = current_node.next
            print(table)
        except Exception as e:
            print("+=================================================+")
            print("Error:", str(e))
            print("+=================================================+")
            
            
    def tambah_proyek(self, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai):
        cursor = mydb.cursor()
        try:
            cursor.execute("SELECT MAX(ID_proyek) FROM proyek")
            max_id = cursor.fetchone()[0]
            if max_id is None:
                max_id = 0
            id_proyek_baru = max_id + 1
            
            query = "INSERT INTO proyek (ID_proyek, deskripsi, nama, anggaran, status, ID_manajer, tanggal_mulai, tanggal_selesai) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (id_proyek_baru, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai)
            cursor.execute(query, values)
            mydb.commit()
            
            self.tambah_di_akhir((id_proyek_baru, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai))
            
            print("+=================================================+")
            print("|          Proyek berhasil ditambahkan.           |")
            print("+=================================================+")
            input("Tekan Enter untuk melanjutkan...")
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
    def tambah_tugas(self, nama, deskripsi, status, tenggat, id_proyek):
        cursor = mydb.cursor() 
        try:
            cursor.execute("SELECT MAX(ID_tugas) FROM tugas")
            max_id = cursor.fetchone()[0]
            if max_id is None:
                max_id = 0
            id_tugas_baru = max_id + 1
            
            query = "INSERT INTO tugas (ID_tugas, nama, deskripsi, status, tenggat, ID_proyek) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (id_tugas_baru, nama, deskripsi, status, tenggat, id_proyek)
            cursor.execute(query, values)
            mydb.commit()
            
            self.tambah_di_akhir((id_tugas_baru, nama, deskripsi, status, tenggat, id_proyek))
            
            print("+=================================================+")
            print("|           Tugas berhasil ditambahkan.           |")
            print("+=================================================+")
            
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
    def tambah_proyek_update(self, deskripsi, tanggal_update, id_proyek):
        cursor = mydb.cursor()
            
        try:
            cursor.execute("SELECT MAX(ID_update) FROM proyek_update")
            max_id = cursor.fetchone()[0]
            if max_id is None:
                max_id = 0
            id_update_baru = max_id + 1
            
            query = "INSERT INTO proyek_update (ID_update, deskripsi, tanggal_update, ID_proyek) VALUES (%s, %s, %s, %s)"
            values = (id_update_baru, deskripsi, tanggal_update, id_proyek)
            cursor.execute(query, values)
            mydb.commit()
            
            self.tambah_di_akhir((id_update_baru, deskripsi, tanggal_update, id_proyek))
            
            print("+=================================================+")
            print("|          Proyek Update berhasil ditambahkan.    |")
            print("+=================================================+")
            
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
    def hapus_proyek(self, id_proyek):
        cursor = mydb.cursor()
        try:
            query_hapus_karyawan = "DELETE FROM karyawan WHERE ID_tugas IN (SELECT ID_tugas FROM tugas WHERE ID_proyek = %s)"
            cursor.execute(query_hapus_karyawan, (id_proyek,))
            
            query_hapus_tugas = "DELETE FROM tugas WHERE ID_proyek = %s"
            cursor.execute(query_hapus_tugas, (id_proyek,))
            
            query_hapus_proyek_update = "DELETE FROM proyek_update WHERE ID_proyek = %s"
            cursor.execute(query_hapus_proyek_update, (id_proyek,))
            
            query_hapus_proyek = "DELETE FROM proyek WHERE ID_proyek = %s"
            cursor.execute(query_hapus_proyek, (id_proyek,))
            mydb.commit()
            
            row_count = cursor.rowcount
            if row_count > 0:
                current_node = self.head
                prev_node = None
                while current_node:
                    if current_node.data[0] == id_proyek:
                        if prev_node:
                            prev_node.next = current_node.next
                        else:
                            self.head = current_node.next
                        break
                    prev_node = current_node
                    current_node = current_node.next
                    
                    query_get_tasks = "SELECT * FROM proyek"
                    cursor.execute(query_get_tasks)
                    proyek_diperbarui = cursor.fetchall()
                    
                    self.head = None
                    for proyek in proyek_diperbarui:
                        self.tambah_di_akhir(proyek)
                print("+=================================================+")
                print("|            Proyek berhasil dihapus.             |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                print("\n")
            else:
                print("+=================================================+")
                print("|   Proyek dengan ID tersebut tidak ditemukan.    |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
    def hapus_tugas(self, id_tugas):
        cursor = mydb.cursor()
        try:
            query_hapus_karyawan = "DELETE FROM karyawan WHERE ID_tugas = %s"
            cursor.execute(query_hapus_karyawan, (id_tugas,))

            query_hapus_tugas = "DELETE FROM tugas WHERE ID_tugas = %s"
            cursor.execute(query_hapus_tugas, (id_tugas,))
            mydb.commit()
            
            row_count = cursor.rowcount
            
            if row_count > 0:
                query_get_tasks = "SELECT * FROM tugas"
                cursor.execute(query_get_tasks)
                tugas_diperbarui = cursor.fetchall()
                
                self.head = None
                for tugas in tugas_diperbarui:
                    self.tambah_di_akhir(tugas)
                
                print("+=================================================+")
                print("|            Tugas berhasil dihapus.              |")
                print("+=================================================+")
            else:
                print("+=================================================+")
                print("|       Tugas dengan ID tersebut tidak ditemukan. |")
                print("+=================================================+")
                
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
    def hapus_proyek_update(self, id_proyek_update):
        cursor = mydb.cursor()
            
        try:
            query_hapus_proyek_update = "DELETE FROM proyek_update WHERE ID_update = %s"
            cursor.execute(query_hapus_proyek_update, (id_proyek_update,))
            mydb.commit()
            
            row_count = cursor.rowcount
            
            if row_count > 0:
                query_get_proyek_update = "SELECT * FROM proyek_update"
                cursor.execute(query_get_proyek_update)
                proyek_update_diperbarui = cursor.fetchall()
                
                self.head = None
                for proyek_update in proyek_update_diperbarui:
                    self.tambah_di_akhir(proyek_update)
                
                print("+=================================================+")
                print("|       Proyek Update berhasil dihapus.          |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("+=================================================+")
                print("|       Proyek Update tidak ditemukan.           |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
    def perbarui_tugas(self, id_tugas, nama, deskripsi, status, tenggat, id_proyek):
        cursor = mydb.cursor()
        try:
            query = "UPDATE tugas SET nama = %s, deskripsi = %s, status = %s, tenggat = %s, ID_proyek = %s WHERE ID_tugas = %s"
            values = (nama, deskripsi, status, tenggat, id_proyek, id_tugas)
            cursor.execute(query, values)
            mydb.commit()
            
            if cursor.rowcount > 0:
                current_node = self.head
                while current_node is not None:
                    if current_node.data[0] == id_tugas:
                        current_node.data = (id_tugas, nama, deskripsi, status, tenggat, id_proyek)
                        break
                    current_node = current_node.next
                        
                query_get_tasks = "SELECT * FROM tugas"
                cursor.execute(query_get_tasks)
                tugas_diperbarui = cursor.fetchall()
                    
                self.head = None
                for tugas in tugas_diperbarui:
                    self.tambah_di_akhir(tugas)
                    
                print("+=================================================+")
                print("|            Tugas berhasil diperbarui.           |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("+=================================================+")
                print("|            ID Tugas tidak ditemukan.            |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
    def perbarui_proyek(self, id_proyek, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai):
        cursor = mydb.cursor()
        try:
            query = "UPDATE proyek SET deskripsi = %s, nama = %s, anggaran = %s, status = %s, ID_manajer = %s, tanggal_mulai = %s, tanggal_selesai = %s WHERE ID_proyek = %s"
            values = (deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai, id_proyek)
            cursor.execute(query, values)
            mydb.commit()
            
            if cursor.rowcount > 0:
                current_node = self.head
                while current_node is not None:
                    if current_node.data[0] == id_proyek:
                        current_node.data = (id_proyek, deskripsi, nama, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai)
                        break
                    current_node = current_node.next
                        
                query_get_proyek = "SELECT * FROM proyek"
                cursor.execute(query_get_proyek)
                proyek_diperbarui = cursor.fetchall()
                    
                self.head = None
                for proyek in proyek_diperbarui:
                    self.tambah_di_akhir(proyek)
                    
                print("+=================================================+")
                print("|           Proyek berhasil diperbarui.           |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("+=================================================+")
                print("|           ID Proyek tidak ditemukan.            |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
    def perbarui_proyek_update(self, id_proyek_update, deskripsi, tanggal_update, id_proyek):
        cursor = mydb.cursor()
        try:
            query = "UPDATE proyek_update SET deskripsi = %s, tanggal_update = %s, ID_proyek = %s WHERE ID_update = %s"
            values = (deskripsi, tanggal_update, id_proyek, id_proyek_update)
            cursor.execute(query, values)
            mydb.commit()
            
            if cursor.rowcount > 0:
                current_node = self.head
                while current_node is not None:
                    if current_node.data[0] == id_proyek_update:
                        current_node.data = (id_proyek_update, deskripsi, tanggal_update, id_proyek)
                        break
                    current_node = current_node.next
                        
                query_get_proyek_update = "SELECT * FROM proyek_update"
                cursor.execute(query_get_proyek_update)
                proyek_update_diperbarui = cursor.fetchall()
                    
                self.head = None
                for proyek_update in proyek_update_diperbarui:
                    self.tambah_di_akhir(proyek_update)
                    
                print("+=================================================+")
                print("|       Proyek Update berhasil diperbarui.        |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("+=================================================+")
                print("|      ID Proyek Update tidak ditemukan.          |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                    
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
    def edit_status(self, id_tugas, status):
        cursor = mydb.cursor()
        try:
            query = "UPDATE tugas SET status = %s WHERE ID_tugas = %s"
            values = (status, id_tugas)
            cursor.execute(query, values)
            mydb.commit()
            
            current_node = self.head
            while current_node is not None:
                if current_node.data[0] == id_tugas:
                    current_node.data = (id_tugas, status)
                    break
                current_node = current_node.next
                    
            query_get_tasks = "SELECT * FROM tugas"
            cursor.execute(query_get_tasks)
            tugas_diperbarui = cursor.fetchall()
                    
            self.head = None
            for tugas in tugas_diperbarui:
                self.tambah_di_akhir(tugas)
            
            if tugas_diperbarui:
                print("+=================================================+")
                print("|            Tugas berhasil diperbarui.           |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("+=================================================+")
                print("|            ID Tugas tidak ditemukan.            |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            mydb.rollback()
        finally:
            cursor.close()
            
            
            
    def quick_sort(self, arr, col):
            if len(arr) <= 1:
                return arr
            else:
                pivot = arr[0]
                less_than_pivot = [x for x in arr[1:] if x[col] < pivot[col]]
                greater_than_pivot = [x for x in arr[1:] if x[col] >= pivot[col]]
                return self.quick_sort(less_than_pivot, col) + [pivot] + self.quick_sort(greater_than_pivot, col)
                
    def sort_proyek_by_anggaran(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM proyek")
        result = mycursor.fetchall()
        arr = self.quick_sort(result, 3) 
        self.head = None
        for item in arr:
            self.tambah_di_akhir(item)
            
    def sort_tugas_by_tenggat(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tugas")
        result = mycursor.fetchall()
        arr = self.quick_sort(result, 4)
        self.head = None
        for item in arr:
            self.tambah_di_akhir(item)
            
    def sort_proyek_update_by_tanggal(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM proyek_update")
        result = mycursor.fetchall()
        arr = self.quick_sort(result, 2) 
        self.head = None
        for item in arr:
            self.tambah_di_akhir(item)
        
def cs():
    os.system('cls') 

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
        try:
            print("+=================================================+")
            print("|                    Menu Karyawan                |")
            print("+=================================================+")
            print("|            1. Lihat Daftar Tugas                |")
            print("|            2. Edit Status Tugas                 |")
            print("|            3. Cari Tugas                        |")
            print("|            4. Urut Tugas                        |")
            print("|            5. Lihat Proyek Update               |")
            print("|            6. Kembali                           |")
            print("+=================================================+")
            pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")
            if pilihan == "1":
                cs()
                linked_list_tugas.tampilkan_semua_tugas()
                input("Tekan Enter untuk melanjutkan...")
                cs()
            elif pilihan == "2":
                cs()
                linked_list_tugas.tampilkan_semua_tugas()
                print("+=================================================+")
                print("|                Edit Status Tugas                |")
                print("+=================================================+")
                id_tugas = int(input("Masukkan ID Tugas yang akan diperbarui: ")).strip()
                if id_tugas > 0:
                    print("Status")
                    print("1.Dalam Pengerjaan")
                    print("2.Selesai")
                    status = input("Masukkan Status Tugas: ").strip()
                    if status not in ["1", "2"]:
                        print("+=================================================+")
                        print("|   Data tidak valid. Periksa kembali input Anda! |")
                        print("+=================================================+")
                        continue
                    linked_list_tugas.edit_status(id_tugas, "Dalam Pengerjaan" if status == "1" else "Selesai")
                else:
                    print("+=================================================+")
                    print("|   Data tidak valid. Periksa kembali input Anda! |")
                    print("+=================================================+")
            elif pilihan == "3":
                print("+=================================================+")
                print("|                   Cari Tugas                    |")
                print("+=================================================+")
                nama_tugas = input("Masukkan Nama Tugas yang akan dicari: ")
                linked_list_tugas.cari_tugas(nama_tugas)
                input("Tekan Enter untuk melanjutkan...")
                cs()
                menu_karyawan()
                break
            elif pilihan == "4":
                cs()
                print("+=========================================================================================================================================+")
                print("|                                               Mengurutkan Tugas Berdasarkan Tenggat Tugas                                               |")
                print("+=========================================================================================================================================+")
                linked_list_tugas.sort_tugas_by_tenggat()
                linked_list_tugas.tampilkan_semua_tugas()
                input("Tekan Enter untuk melanjutkan...")
                cs()
                menu_karyawan()
                break
            elif pilihan == "5":
                cs()
                linked_list_proyek_update.tampilkan_proyek_update()
                input("Tekan Enter untuk melanjutkan...")
            elif pilihan == "6":
                cs()
                menu_login()
                break
            else:
                cs()
                print("+=================================================+")
                print("| Pilihan tidak valid. Silakan masukkan angka 1-6.|")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                cs()
        except (KeyboardInterrupt, EOFError, ValueError):
            print("\n-> PERHATIKAN INPUT\n")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
                
                
def menu_manajer():
    while True:
        try:
            print("+=================================================+")
            print("|                    Menu Manajer                 |")
            print("+=================================================+")
            print("|                 1. Kelola Proyek                |")
            print("|                 2. Kembali                      |")
            print("+=================================================+")
            pilihan = input("Masukkan pilihan (1/2/3): ")
            if pilihan == "1":
                cs()
                menu_crud_proyek()
                break
            elif pilihan == "2":
                cs()
                menu_login()
                break
            else:
                cs()
                print("+=================================================+")
                print("| Pilihan tidak valid. Silakan masukkan angka 1/2.|")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                cs()
        except (KeyboardInterrupt, EOFError, ValueError):
            print("\n-> PERHATIKAN INPUT\n")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            
            
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
        try:
            print("\n")
            print("+=================================================+")
            print("|              Menu Penglolaan Proyek             |")
            print("+=================================================+")
            print("|       1. Tambah Proyek                          |")
            print("|       2. Hapus Proyek                           |")
            print("|       3. Perbarui Proyek                        |")
            print("|       4. Cari Proyek                            |")
            print("|       5. Urutkan Proyek                         |")
            print("|       6. Tampilkan Semua Proyek                 |")
            print("|       7. Kelola Tugas                           |")
            print("|       8. Kelola Proyek Update                   |")
            print("|       9. Kembali                                |")
            print("+=================================================+")
            pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7/8): ").strip()
            if pilihan == "1":
                cs()
                print("+=================================================+")
                print("|                   Tambah Proyek                 |")
                print("+=================================================+")
                nama = input("Masukkan Nama Proyek: ").strip()
                deskripsi = input("Masukkan Deskripsi Proyek: ").strip()
                anggaran = input("Masukkan Anggaran Proyek: ").strip()
                print("Status")
                print("1.Dalam Pengerjaan")
                print("2.Selesai")
                status = input("Masukkan Status Proyek: ").strip()
                id_manajer = input("Masukkan ID Manajer Proyek: ").strip()
                tanggal_mulai = input("Masukkan Tanggal Mulai Proyek (YYYY-MM-DD): ").strip()
                tanggal_selesai = input("Masukkan Tanggal Selesai Proyek (YYYY-MM-DD): ").strip()
                
                if not all([nama, deskripsi, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai]):
                    
                    print("+=================================================+")
                    print("|   Semua input harus diisi. Tidak boleh kosong!  |")
                    print("+=================================================+")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                    
                if not anggaran.isdigit() or float(anggaran) < 0 or status not in ["1", "2"]:
                    print("+=================================================+")
                    print("|   Data tidak valid. Periksa kembali input Anda! |")
                    print("+=================================================+")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                    
                cursor = mydb.cursor()
                query = "SELECT * FROM manajer WHERE ID_manajer = %s"
                cursor.execute(query, (id_manajer,))
                result = cursor.fetchone()
                cursor.close()
                if not result:
                    print("+=================================================+")
                    print("|        ID Manajer Proyek tidak ditemukan.       |")
                    print("+=================================================+")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                    
                try:
                    datetime.strptime(tanggal_mulai, "%Y-%m-%d")
                    datetime.strptime(tanggal_selesai, "%Y-%m-%d")
                except ValueError:
                    print("+=================================================+")
                    print("| Format tanggal salah. Gunakan format YYYY-MM-DD.|")
                    print("+=================================================+")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                    
                if datetime.strptime(tanggal_selesai, "%Y-%m-%d") < datetime.strptime(tanggal_mulai, "%Y-%m-%d"):
                    print("+=============================================================+")
                    print("|  Tanggal selesai tidak boleh lebih awal dari tanggal mulai. |")
                    print("+=============================================================+")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                linked_list_proyek.tambah_proyek(deskripsi, nama, float(anggaran), "Dalam Pengerjaan" if status == "1" else "Selesai", id_manajer, tanggal_mulai, tanggal_selesai)
            elif pilihan == "2":
                cs()
                linked_list_proyek.tampilkan_semua_proyek()
                print("+=================================================+")
                print("|                    Hapus Proyek                 |")
                print("+=================================================+")
                id_proyek = input("Masukkan ID Proyek yang akan dihapus: ").strip()
                linked_list_proyek.hapus_proyek(id_proyek)
            elif pilihan == "3":
                cs()
                linked_list_proyek.tampilkan_semua_proyek()
                print("+=================================================+")
                print("|                   Perbarui Proyek               |")
                print("+=================================================+")
                id_proyek = input("Masukkan ID Proyek yang akan diperbarui: ").strip()
                nama = input("Masukkan Nama Proyek: ").strip()
                deskripsi = input("Masukkan Deskripsi Proyek: ").strip()
                anggaran = input("Masukkan Anggaran Proyek: ").strip()
                print("Status")
                print("1.Dalam Pengerjaan")
                print("2.Selesai")
                status = input("Masukkan Status Proyek: ").strip()
                id_manajer = input("Masukkan ID Manajer Proyek: ").strip()
                tanggal_mulai = input("Masukkan Tanggal Mulai Proyek (YYYY-MM-DD): ").strip()
                tanggal_selesai = input("Masukkan Tanggal Selesai Proyek (YYYY-MM-DD): ").strip()
                
                if not all([nama, deskripsi, anggaran, status, id_manajer, tanggal_mulai, tanggal_selesai]):
                    print("+=================================================+")
                    print("|   Semua input harus diisi. Tidak boleh kosong!  |")
                    print("+=================================================+")
                    continue
                    
                if not anggaran.isdigit() or float(anggaran) < 0 or status not in ["1", "2"]:
                    print("+=================================================+")
                    print("|  Data tidak valid. Periksa kembali input Anda!  |")
                    print("+=================================================+")
                    continue
                    
                cursor = mydb.cursor()
                query = "SELECT * FROM manajer WHERE ID_manajer = %s"
                cursor.execute(query, (id_manajer,))
                result = cursor.fetchone()
                cursor.close()
                if not result:
                    print("+=================================================+")
                    print("|     ID Manajer Proyek tidak ditemukan.          |")
                    print("+=================================================+")
                    continue
                try:
                    datetime.strptime(tanggal_mulai, "%Y-%m-%d")
                    datetime.strptime(tanggal_selesai, "%Y-%m-%d")
                except ValueError:
                    print("+=================================================+")
                    print("| Format tanggal salah. Gunakan format YYYY-MM-DD.|")
                    print("+=================================================+")
                    continue
                    
                if datetime.strptime(tanggal_selesai, "%Y-%m-%d") < datetime.strptime(tanggal_mulai, "%Y-%m-%d"):
                    print("+=============================================================+")
                    print("|  Tanggal selesai tidak boleh lebih awal dari tanggal mulai. |")
                    print("+=============================================================+")
                    continue
                linked_list_proyek.perbarui_proyek(id_proyek, deskripsi, nama, float(anggaran), "Dalam Pengerjaan" if status == "1" else "Selesai", id_manajer, tanggal_mulai, tanggal_selesai)
            elif pilihan == "4":
                cs()
                print("+=================================================+")
                print("|                    Cari Proyek                  |")
                print("+=================================================+")
                nama_proyek = input("Masukkan Nama Proyek yang akan dicari: ").strip()
                linked_list_proyek.cari_proyek(nama_proyek)
                input("Tekan Enter untuk kembali...")
                cs()
                menu_crud_proyek()
                break
            elif pilihan == "5":
                cs()
                print("+=========================================================================================================================================+")
                print("|                                               Mengurutkan Proyek Berdasarkan Anggaran Proyek                                            |")
                print("+=========================================================================================================================================+")
                linked_list_proyek.sort_proyek_by_anggaran()
                linked_list_proyek.tampilkan_semua_proyek()
                input("Tekan Enter untuk kembali...")
                cs()
                menu_crud_proyek()
                break
            elif pilihan == "6":
                cs()
                linked_list_proyek.tampilkan_semua_proyek()
                input("Tekan Enter untuk kembali...")
                cs()
            elif pilihan == "7":
                cs()
                menu_crud_tugas()
                break
            elif pilihan == "8":
                cs()
                menu_crud_proyek_update()
                break
            elif pilihan == "9":
                cs()
                menu_manajer()
                break
            else:
                print("+=================================================+")
                print("| Pilihan tidak valid. Silakan masukkan angka 1-8.|")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                cs()
        except (KeyboardInterrupt, EOFError, ValueError):
            print("\n-> PERHATIKAN INPUT\n")
            input("Tekan Enter untuk melanjutkan...")
            cs()
        except Exception as e:
                print(f"Terjadi kesalahan: {e}")
                
                
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
        try:
            print("\n")
            print("+=================================================+")
            print("|              Menu Pengelolaan Tugas             |")
            print("+=================================================+")
            print("|       1. Tambah Tugas                           |")
            print("|       2. Hapus Tugas                            |")
            print("|       3. Perbarui Tugas                         |")
            print("|       4. Cari Tugas                             |")
            print("|       5. Urutkan Tugas                          |")
            print("|       6. Tampilkan Semua Tugas                  |")
            print("|       7. Kembali                                |")
            print("+=================================================+")
            pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ").strip()
            
            if pilihan == "1":
                print("+=================================================+")
                print("|                   Tambah Tugas                  |")
                print("+=================================================+")
                nama = input("Masukkan Nama Tugas: ").strip()
                deskripsi = input("Masukkan Deskripsi Tugas: ").strip()
                tenggat = input("Masukkan Tenggat Tugas (YYYY-MM-DD): ").strip()
                print("Status")
                print("1.Dalam Pengerjaan")
                print("2.Selesai")
                status = input("Masukkan Status Tugas: ").strip()
                id_proyek = input("Masukkan ID Proyek: ").strip()
                
                if not all([nama, deskripsi, tenggat, status,  id_proyek]):
                    print("+=================================================+")
                    print("|   Semua input harus diisi. Tidak boleh kosong!  |")
                    print("+=================================================+")
                    continue
                    
                if status not in ["1", "2"]:
                    print("+=================================================+")
                    print("|   Data tidak valid. Periksa kembali input Anda! |")
                    print("+=================================================+")
                    continue
                try:
                    datetime.strptime(tenggat, "%Y-%m-%d")
                except ValueError:
                    print("+=================================================+")
                    print("| Format tanggal salah. Gunakan format YYYY-MM-DD.|")
                    print("+=================================================+")
                    continue
                    
                cursor = mydb.cursor()
                query_proyek = "SELECT * FROM proyek WHERE ID_proyek = %s"
                cursor.execute(query_proyek, (id_proyek,))
                result_proyek = cursor.fetchone()
                cursor.close()
                    
                if not result_proyek:
                    print("+=================================================+")
                    print("|    ID Proyek tidak ditemukan.                   |")
                    print("+=================================================+")
                    continue
                linked_list_tugas.tambah_tugas(nama, deskripsi, "Dalam Pengerjaan" if status == "1" else "Selesai",tenggat, id_proyek)
            elif pilihan == "2":
                linked_list_tugas.tampilkan_semua_tugas()
                print("+=================================================+")
                print("|                    Hapus Tugas                  |")
                print("+=================================================+")
                id_tugas = input("Masukkan ID Tugas yang akan dihapus: ")
                linked_list_tugas.hapus_tugas(id_tugas)
            elif pilihan == "3":
                linked_list_tugas.tampilkan_semua_tugas()
                print("+=================================================+")
                print("|                 Perbarui Tugas                  |")
                print("+=================================================+")
                id_tugas = input("Masukkan ID Tugas yang akan diperbarui: ").strip()
                nama = input("Masukkan Nama Tugas: ").strip()
                deskripsi = input("Masukkan Deskripsi Tugas: ").strip()
                print("Status")
                print("1.Dalam Pengerjaan")
                print("2.Selesai")
                status = input("Masukkan Status Tugas: ").strip()
                tenggat = input("Masukkan Tenggat Tugas (YYYY-MM-DD): ").strip()
                id_proyek = input("Masukkan ID Proyek Pelaksana: ").strip()
                
                if not all([nama, deskripsi, status, tenggat, id_proyek]):
                    print("+=================================================+")
                    print("|   Semua input harus diisi. Tidak boleh kosong!  |")
                    print("+=================================================+")
                    input("Tekan Enter untuk melanjutkan...")   
                    continue
                    
                if status not in ["1", "2"]:
                    print("+=================================================+")
                    print("|             Status harus 1 atau 2.              |")
                    print("+=================================================+")
                    continue
                try:
                    datetime.strptime(tenggat, "%Y-%m-%d")
                except ValueError:
                    print("+=================================================+")
                    print("| Format tanggal salah. Gunakan format YYYY-MM-DD.|")
                    print("+=================================================+")
                    continue
                    
                cursor = mydb.cursor()
                query_proyek = "SELECT * FROM proyek WHERE ID_proyek = %s"
                cursor.execute(query_proyek, (id_proyek,))
                result_proyek = cursor.fetchone()
                cursor.close()
                    
                if not result_proyek:
                    print("+=================================================+")
                    print("|             ID Proyek tidak ditemukan.          |")
                    print("+=================================================+")
                    continue
                linked_list_tugas.perbarui_tugas(id_tugas, nama, deskripsi, "Dalam Pengerjaan" if status == "1" else "Selesai", tenggat, id_proyek)
            elif pilihan == "4":
                print("+=================================================+")
                print("|                    Cari Tugas                   |")
                print("+=================================================+")
                nama_tugas = input("Masukkan Nama Tugas yang akan dicari: ")
                linked_list_tugas.cari_tugas(nama_tugas)
                input("Tekan Enter untuk kembali...")
                cs()
                menu_crud_tugas()
                break
            elif pilihan == "5":
                cs()
                print("+=========================================================================================================================================+")
                print("|                                               Mengurutkan Tugas Berdasarkan Tenggat Tugas                                               |")
                print("+=========================================================================================================================================+")
                linked_list_tugas.sort_tugas_by_tenggat()
                linked_list_tugas.tampilkan_semua_tugas()
                input("Tekan Enter untuk kembali...")
                cs()
                menu_crud_tugas()
                break
            elif pilihan == "6":
                cs()
                linked_list_tugas.tampilkan_semua_tugas()
                input("Tekan Enter untuk kembali...")
            elif pilihan == "7":
                cs()
                menu_manajer()
                break
            else:
                cs()
                print("+=================================================+")
                print("| Pilihan tidak valid. Silakan masukkan angka 1-6.|")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                cs()
        except (KeyboardInterrupt, EOFError, ValueError):
            print("\n-> PERHATIKAN INPUT\n")
        except Exception as e:
                print(f"Terjadi kesalahan: {e}")
                
                
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
        try:
            print("\n")
            print("+=================================================+")
            print("|           Menu Pengelolaan Proyek update        |")
            print("+=================================================+")
            print("|       1. Tambah proyek update                   |")
            print("|       2. Hapus proyek update                    |")
            print("|       3. Perbarui proyek update                 |")
            print("|       4. Cari proyek update                     |")
            print("|       5. Urutkan proyek update                  |")
            print("|       6. Tampilkan Semua proyek update          |")
            print("|       7. Kembali                                |")
            print("+=================================================+")
            pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")
            if pilihan == "1":
                print("+=================================================+")
                print("|               Tambah Proyek Update              |")
                print("+=================================================+")
                deskripsi = input("Masukkan Deskripsi Proyek: ").strip()
                tanggal_update = input("Masukkan tanggal update (YYYY-MM-DD): ").strip()
                id_proyek = input("Masukkan Id proyek: ").strip()
                
                cursor = mydb.cursor()
                query_check_proyek = "SELECT * FROM proyek WHERE ID_proyek = %s"
                cursor.execute(query_check_proyek, (id_proyek,))
                result_proyek = cursor.fetchone()
                cursor.close()
                    
                if not result_proyek:
                    print("+=================================================+")
                    print("|              ID Proyek tidak ditemukan.         |")
                    print("+=================================================+")
                    continue
                    
                if not all([deskripsi, tanggal_update, id_proyek]):
                    print("+=================================================+")
                    print("|   Semua input harus diisi. Tidak boleh kosong!  |")
                    print("+=================================================+")
                    continue
                try:
                    datetime.strptime(tanggal_update, "%Y-%m-%d")
                except ValueError:
                    print("+=================================================+")
                    print("| Format tanggal salah. Gunakan format YYYY-MM-DD.|")
                    print("+=================================================+")
                    continue
                linked_list_proyek_update.tambah_proyek_update(deskripsi, tanggal_update, id_proyek)
            elif pilihan == "2":
                linked_list_proyek_update.tampilkan_proyek_update
                print("+=================================================+")
                print("|               Hapus Proyek Update               |")
                print("+=================================================+")
                id_proyek_update = input("Masukkan ID proyek update yang akan dihapus: ").strip()
                linked_list_proyek_update.hapus_proyek_update(id_proyek_update)
            elif pilihan == "3":
                print("+=================================================+")
                print("|              Perbarui Proyek Update             |")
                print("+=================================================+")
                id_proyek_update = input("Masukkan ID proyek update: ").strip()
                deskripsi = input("Masukkan Deskripsi Proyek: ").strip()
                tanggal_update = input("Masukkan tanggal update (YYYY-MM-DD): ").strip()
                id_proyek = input("Masukkan Id proyek: ").strip()
                
                cursor = mydb.cursor()
                query_check_proyek = "SELECT * FROM proyek WHERE ID_proyek = %s"
                cursor.execute(query_check_proyek, (id_proyek,))
                result_proyek = cursor.fetchone()
                cursor.close()
                    
                if not result_proyek:
                    print("+=================================================+")
                    print("|    ID Proyek tidak ditemukan.                   |")
                    print("+=================================================+")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                    
                if not all([deskripsi, tanggal_update, id_proyek]):
                    print("+=================================================+")
                    print("|   Semua input harus diisi. Tidak boleh kosong!  |")
                    print("+=================================================+")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                try:
                    datetime.strptime(tanggal_update, "%Y-%m-%d")
                except ValueError:
                    print("+=================================================+")
                    print("| Format tanggal salah. Gunakan format YYYY-MM-DD.|")
                    print("+=================================================+")
                    continue
                linked_list_proyek_update.perbarui_proyek_update(id_proyek_update, deskripsi, tanggal_update, id_proyek)
            elif pilihan == "4":
                print("+=================================================+")
                print("|               Cari Proyek Update                |")
                print("+=================================================+")
                nama_proyek_update = input("Masukkan Nama proyek update yang akan dicari: ").strip()
                linked_list_proyek_update.cari_proyek_update(nama_proyek_update)
                input("Tekan Enter untuk kembali...")
                cs()
                menu_crud_proyek_update()
                break
            elif pilihan == "5":
                cs()
                print("+=========================================================================================================================================+")
                print("|                                     Mengurutkan Proyek Update Berdasarkan Tanggal Update Proyek                                         |")
                print("+=========================================================================================================================================+")
                linked_list_proyek_update.sort_proyek_update_by_tanggal()
                linked_list_proyek_update.tampilkan_proyek_update()
                input("Tekan Enter untuk kembali...")
                cs()
                menu_crud_proyek_update()
                break
            elif pilihan == "6":
                cs()
                linked_list_proyek_update.tampilkan_proyek_update()
                input("Tekan Enter untuk kembali...")
                cs()
            elif pilihan == "7":
                cs()
                menu_manajer()
                break
            else:
                cs()
                print("+=================================================+")
                print("| Pilihan tidak valid. Silakan masukkan angka 1-6.|")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                cs()
        except (KeyboardInterrupt, EOFError, ValueError):
            print("\n-> PERHATIKAN INPUT\n")
        except Exception as e:
                print(f"Terjadi kesalahan: {e}")
                
                
#Untuk Login
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
        
#sampe sini untuk loginnya
        
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
        try:
            print("+=================================================+")
            print("|                    Menu Login                   |")
            print("+=================================================+")
            print("|                   1. Karyawan                   |")
            print("|                   2. Manajer                    |")
            print("|                   3. Keluar                     |")
            print("+=================================================+")
            pilihan = input("Masukkan pilihan (1/2/3): ")
            if pilihan == "1":
                email_karyawan = input("Masukkan Email Karyawan: ")
                if cek_email_karyawan(email_karyawan) :
                    pw = int(input("Masukkan ID Karyawan: "))
                    if validasi_login_karyawan(email_karyawan, pw):
                        cs()
                        print("+=================================================+")
                        print(f" Login berhasil! Selamat datang, {ambil_nama_karyawan(email_karyawan, pw)}  ")
                        print("+=================================================+")
                        menu_karyawan()
                        break
                    else:
                        print("+=================================================+")
                        print("|  ID atau email salah atau Anda bukan  karyawan. |")
                        print("+=================================================+")
                        input("Tekan Enter untuk melanjutkan...")
                else:
                    print("+=================================================+")
                    print("|  ID atau email salah atau Anda bukan karyawan.  |")
                    print("+=================================================+")
                    input("Tekan Enter untuk melanjutkan...")
                    cs()
            elif pilihan == "2":
                email_manajer = input("Masukkan Email Manajer: ")
                if cek_email_manajer(email_manajer) :
                    pw = int(input("Masukkan ID Manajer: "))
                    if validasi_login_manajer(email_manajer, pw):
                        cs()
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
                        input("Tekan Enter untuk melanjutkan...")
                else:
                    print("+=================================================+")
                    print("|   ID atau email salah atau Anda bukan manajer.  |")
                    print("+=================================================+")
                    input("Tekan Enter untuk melanjutkan...")
            elif pilihan == "3":
                cs()
                print("+=================================================+")
                print("|        Anda telah keluar dari aplikasi          |")
                print("+=================================================+")
                break
            else:
                print("+=================================================+")
                print("|  Pilihan tidak valid. Silakan masukkan 1/2/3.   |")
                print("+=================================================+")
                input("Tekan Enter untuk melanjutkan...")
                cs()
        except (KeyboardInterrupt, EOFError, ValueError):
            print("\n-> PERHATIKAN INPUT\n")
        except Exception as e:
                print(f"Terjadi kesalahan: {e}")
cs()
print('''
+=================================================+
|            +        Aplikasi         +          |
|         Sistem Manajemen Proyek Perusahaan      |
+=================================================+
''')
menu_login()