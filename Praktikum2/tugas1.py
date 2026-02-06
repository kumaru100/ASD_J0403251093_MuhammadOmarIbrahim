# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Muhammad Omar Ibrahim
# NIM   : J0403251093
# Kelas : B1
# ========================================================== 
# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt" 
# ------------------------------- 
# Fungsi: Membaca data dari file 
# ------------------------------- 
def baca_stok(nama_file): 
    '''
Membaca data stok dari file teks. 
Format per baris: KodeBarang,NamaBarang,Stok 
Output: - stok_dict (dictionary) 
key   = kode_barang 
value = {"nama": nama_barang, "stok": stok_int} 
''' 
    stok_dict = {} 
    with open(nama_file, "r", encoding="utf-8") as f:
        for baris in f:
            baris = baris.strip()
            KodeBarang,NamaBarang,Stok = baris.split(",")
            
            stok_dict[KodeBarang] = {
                "nama": NamaBarang,
                "stok": int(Stok),
            }

    return stok_dict 


# ------------------------------- 
# Fungsi: Menyimpan data ke file 
# ------------------------------- 
buka_data = baca_stok(NAMA_FILE)
def simpan_stok(nama_file, stok_dict): 
    """ 
Menyimpan seluruh data stok ke file teks. 
Format per baris: KodeBarang,NamaBarang,Stok 
""" 
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in stok_dict:
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}\n")


# TODO: Tulis ulang seluruh isi file berdasarkan stok_dict 
# Hint: with open(nama_file, "w", encoding="utf-8") as f: 


# ------------------------------- 
# Fungsi: Menampilkan semua data 
# ------------------------------- 
def tampilkan_semua(stok_dict): 
    """
Menampilkan semua barang di stok_dict. 
"""
    if len(stok_dict) == 0: 
        print("Stok barang kosong!") 
        return
    print("\n========== Daftar Stok Kantin ==========")
    print(f"{'KODE':10} {'| NAMA':<20} {'| STOK':>5}")
    print("-" *40)

    for kode in sorted(stok_dict.keys()):
        nama_barang = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:10} {nama_barang:<20} {stok:>5}")
    

# TODO: Jika kosong, tampilkan pesan stok kosong 
# TODO: Tampilkan dengan format rapi: kode | nama | stok 



# ------------------------------- 
# Fungsi: Cari barang berdasarkan kode 
# ------------------------------- 
def cari_barang(stok_dict): 
    """ 
Mencari barang berdasarkan kode barang. 
""" 
    kode = input("Masukkan kode barang: ").strip() 
    if kode in stok_dict:
        nama_barang = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print("========== Barang Ditemukan ==========")
        print(f"Kode : {kode}")
        print(f"Nama : {nama_barang}")
        print(f"Stok : {stok}")
    else:
        print("Barang tidak ditemukan.")

# TODO: Cek apakah kode ada di dictionary 
# Jika ada: tampilkan detail barang 
# Jika tidak ada: tampilkan 'Barang tidak ditemukan' 


# ------------------------------- 
# Fungsi: Tambah barang baru 
# ------------------------------- 
def tambah_barang(stok_dict):
    """
Menambah barang baru ke stok_dict.
"""
    #Meminta input
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return
    nama_barang = input("Masukkan nama barang: ").strip()
    stok_awal = int(input("Masukkan stok: ").strip())
    #Simpan ke dictionary
    stok_dict[kode] = {"nama": nama_barang, "stok": stok_awal}
    print("Barang baru berhasil ditambahkan.")

# TODO: Validasi kode tidak boleh duplikat 
# Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return 
# TODO: Input stok awal (integer) 
# Hint: stok_awal = int(input(...)) 
# TODO: Simpan ke dictionary 



# ------------------------------- 
# Fungsi: Update stok barang 
# ------------------------------- 
def update_stok(stok_dict): 
    """ 
Mengubah stok barang (tambah atau kurangi). 
Stok tidak boleh menjadi negatif. 
""" 
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return
    # TODO: Cek apakah kode ada di dictionary 
    # Jika tidak ada: tampilkan pesan dan return 
    print(f"Stok saat ini: {stok_dict[kode]['stok']}")
    print("Pilih jenis update:") 
    print("1. Tambah stok") 
    print("2. Kurangi stok") 

    pilihan = input("Masukkan pilihan (1/2): ").strip() 
    if pilihan not in ["1", "2"]:
        print("Pilihan tidak valid.")
        return
    elif pilihan == "1":
        try:
            print(f"Stok saat ini: {stok_dict[kode]['stok']}")
            jumlah = int(input("Masukkan jumlah yang ditambahkan: ").strip())
        except ValueError:
            print("Jumlah harus berupa angka. Update dibatalkan.")
            return
        if jumlah < 0:
            print("Jumlah harus positif. Update dibatalkan.")
            return
        stok_dict[kode]["stok"] += jumlah
        print(f"Stok barang {kode} berhasil ditambah menjadi {stok_dict[kode]['stok']}.")

    else:
        try:
            print(f"Stok saat ini: {stok_dict[kode]['stok']}")
            jumlah = int(input("Masukkan jumlah yang dikurangi: ").strip())
        except ValueError:
            print("Jumlah harus berupa angka. Update dibatalkan.")
            return
        if jumlah < 0:
            print("Jumlah harus positif. Update dibatalkan.")
            return
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh negatif. Update dibatalkan.")
            return
        stok_dict[kode]["stok"] -= jumlah
        print(f"Stok barang {kode} berhasil dikurangi menjadi {stok_dict[kode]['stok']}.")

    # TODO: Input jumlah perubahan stok 
    # Hint: jumlah = int(input("Masukkan jumlah: ")) 
 
    # TODO: 
    # - Jika pilihan 1: stok = stok + jumlah 
    # - Jika pilihan 2: stok = stok - jumlah 
    # - Jika hasil < 0: batalkan dan tampilkan error 
 
    pass 
 
 
# ------------------------------- 
# Program Utama 
# ------------------------------- 
def main(): 
    # Membaca data dari file saat program mulai 
    stok_barang = baca_stok(NAMA_FILE) 
 
    while True: 
        print("\n========== MENU STOK KANTIN ===============") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 
 
        pilihan = input("Pilih menu: ").strip() 
 
        if pilihan == "1": 
            tampilkan_semua(stok_barang) 
 
        elif pilihan == "2": 
            cari_barang(stok_barang) 
 
        elif pilihan == "3": 
            tambah_barang(stok_barang) 
 
        elif pilihan == "4": 
            update_stok(stok_barang) 
 
        elif pilihan == "5": 
            simpan_stok(NAMA_FILE, stok_barang) 
            print("Data berhasil disimpan.") 
 
        elif pilihan == "0": 
            print("Program selesai.") 
            break 
    else: 
        print("Pilihan tidak valid. Silakan coba lagi.") 
# Menjalankan program utama 
if __name__ == "__main__": 
    main() 