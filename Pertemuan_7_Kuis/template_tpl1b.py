# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Muhammad Omar Ibrahim
# NIM     : J0403251093
# Kelas   : TPL B1
# ==============================================================================


# ==============================================================================
# 1. FILE HANDLING & DICTIONARY
# Fungsi ini digunakan untuk membaca file buku.txt lalu menyimpannya
# ke dalam struktur data Dictionary agar mudah diakses berdasarkan kode buku
# ==============================================================================
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    
    # Dictionary untuk menyimpan seluruh data buku
    database_buku = {}
    
    try:
        # Membuka file dengan mode read (r)
        with open(nama_file, 'r') as file:
            
            # Membaca setiap baris dalam file
            for line in file:
                
                # Menghapus newline lalu memisahkan data berdasarkan koma
                kode, judul, harga = line.strip().split(',')
                
                # Menyimpan data ke dictionary
                # key = kode buku
                # value = dictionary berisi judul dan harga
                database_buku[kode] = {
                    'Judul': judul,
                    'Harga': int(harga)
                }

                # Menampilkan data yang berhasil dibaca
                print(f"Kode: {kode}, Judul: {judul}, Harga: {harga}")

    # Jika file tidak ditemukan
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

    # Menangkap error lain yang mungkin terjadi
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
    
    # Mengembalikan dictionary yang berisi data buku
    return database_buku



# ==============================================================================
# 2. LINKED LIST - MANAJEMEN PROMOSI
# Digunakan untuk menyimpan daftar buku yang sedang dipromosikan
# menggunakan struktur Linked List
# ==============================================================================

# Class Node sebagai elemen dasar Linked List
class Node:
    def __init__(self, judul):
        self.judul = judul   # data yang disimpan (judul buku)
        self.next = None     # pointer ke node berikutnya


class LinkedListPromosi:
    
    # Constructor Linked List
    def __init__(self):
        self.head = None   # node pertama dalam linked list

    # Menambahkan buku ke daftar promosi
    def tambah_buku_promosi(self, judul):
        
        # Membuat node baru
        baru = Node(judul)

        # Jika linked list masih kosong
        if self.head is None:
            self.head = baru
        else:
            # Jika sudah ada isi, cari node terakhir
            current = self.head
            while current.next:
                current = current.next
            
            # Node baru ditambahkan di akhir list
            current.next = baru

    # Menampilkan seluruh daftar buku promosi
    def tampilkan_promosi(self):
        print("Daftar Buku Promosi:")
        
        current = self.head
        nomor = 1

        # Traversal dari head sampai akhir
        while current:
            print(f"{nomor}. {current.judul}")
            current = current.next
            nomor += 1



# ==============================================================================
# 3. QUEUE - ANTREAN KASIR
# Struktur data Queue digunakan untuk mengelola antrean pelanggan
# dengan konsep FIFO (First In First Out)
# ==============================================================================

class AntreanKasir:
    
    def __init__(self):
        # Node paling depan antrean
        self.front = None
        
        # Node paling belakang antrean
        self.rear = None

    # Mengecek apakah antrean kosong
    def is_empty(self):
        return self.front is None

    # ENQUEUE -> Menambah pelanggan ke antrean
    def tambah_antrean(self, nama_pelanggan):

        # Membuat node baru untuk pelanggan
        antreanBaru = Node(nama_pelanggan)

        # Jika antrean kosong
        if self.is_empty():
            self.front = antreanBaru
            self.rear = antreanBaru
        else:
            # Tambahkan ke belakang antrean
            self.rear.next = antreanBaru
            self.rear = antreanBaru

        print(f"{nama_pelanggan} masuk ke antrean.")

    # DEQUEUE -> Melayani pelanggan paling depan
    def layani_pelanggan(self):
        
        # Jika antrean kosong
        if self.is_empty():
            print("Antrean kosong, tidak ada pelanggan.")
            return

        # Ambil pelanggan paling depan
        pelanggan_dilayani = self.front.judul

        # Geser front ke node berikutnya
        self.front = self.front.next

        # Jika setelah dilayani antrean menjadi kosong
        if self.front is None:
            self.rear = None

        print(f"Pelanggan {pelanggan_dilayani} telah dilayani.")

    # Menampilkan seluruh antrean pelanggan
    def tampilkan_antrean(self):
        
        if self.is_empty():
            print("Antrean kosong.")
            return

        current = self.front
        nomor = 1

        print("Daftar Antrean:")

        # Traversal antrean dari depan ke belakang
        while current:
            print(f"{nomor}. {current.judul}")
            current = current.next
            nomor += 1



# ==============================================================================
# 4. SORTING - LAPORAN TRANSAKSI
# Mengurutkan data transaksi menggunakan algoritma Insertion Sort
# ==============================================================================

def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga menggunakan Insertion Sort
    """

    # Membuat salinan list agar data asli tidak berubah
    hasil = list_harga.copy()

    # Perulangan mulai dari elemen kedua
    for i in range(1, len(hasil)):

        key = hasil[i]   # nilai yang akan disisipkan
        j = i - 1

        # Menggeser elemen yang lebih besar dari key ke kanan
        while j >= 0 and hasil[j] > key:
            hasil[j + 1] = hasil[j]
            j -= 1

        # Menempatkan key pada posisi yang benar
        hasil[j + 1] = key

    # Mengembalikan list yang sudah terurut
    return hasil



# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# Program utama yang menjalankan seluruh fitur sistem
# ==============================================================================

def main():
    
    # Inisialisasi data awal
    
    file_db = "buku.txt"
    
    # Membaca data buku dari file
    data_buku = muat_data_buku(file_db)

    # Membuat objek Linked List promosi
    list_promosi = LinkedListPromosi()

    # Membuat objek antrean kasir
    antrean_toko = AntreanKasir()

    # Contoh data transaksi
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]



    # Loop menu utama
    while True:

        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")



        # MENU 1 -> Menampilkan katalog buku
        if pilihan == '1':
            print("\nKatalog Buku:", data_buku)



        # MENU 2 -> Menambahkan buku ke daftar promosi
        elif pilihan == '2':

            judul = input("Masukkan judul buku untuk promosi: ").strip()

            list_promosi.tambah_buku_promosi(judul)
            list_promosi.tampilkan_promosi()



        # MENU 3 -> Mengelola antrean kasir
        elif pilihan == '3': 

            print("\n1. Tambah Antrean")
            print("2. Layani Pelanggan")
            print("3. Lihat Antrean")

            sub = input("Pilih opsi: ")

            # Tambah pelanggan ke antrean
            if sub == '1':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)

            # Melayani pelanggan terdepan
            elif sub == '2':
                antrean_toko.layani_pelanggan()

            # Menampilkan antrean
            elif sub == '3':
                antrean_toko.tampilkan_antrean()



        # MENU 4 -> Menampilkan laporan transaksi yang sudah diurutkan
        elif pilihan == '4':

            print("Harga Sebelum Urut:", riwayat_transaksi)

            hasil_sort = urutkan_transaksi(riwayat_transaksi)

            print("Harga Sesudah Urut:", hasil_sort)



        # MENU 5 -> Keluar dari program
        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break



        # Jika input menu tidak valid
        else:
            print("Pilihan tidak valid!")



# Menjalankan program utama
if __name__ == "__main__":
    main()