#==========================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan dasar 1 : Membuat fungsi load data
#==========================================
nama_file = "data_mahasiswa.txt"
#Membuat fungsi untuk membaca data mahasiswa dari file

def baca_data_mahasiswa(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim,nama,nilai = baris.split(",")

            #simpan data mahasiswa ke dictionary
            data_dict[nim] = {
                "nama" : nama,
                "nilai" : int(nilai),
            }
    return data_dict 
#memanggil fungsi baca_data_mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
#print("Jumlah record dalam buka data :", len(buka_data))

#===============================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan dasar 2 : Membuat fungsi load data
#===============================================
def tampilkan_data_mahasiswa(data_dict):
    #Error handling
    if len(data_dict) == 0:
        print("Data mahasiswa kosong!")
        return

    #Membuat header tabel
    print("\n======= Daftar Mahasiswa =======")
    print(f"{'NIM':10} {'NAMA':<12} {'NILAI':>5}")
    print("-" *32)
    '''
    untuk tampilan yang rapu, atur f-string formatting
    {"NIM":10} artinya:
    tampilkan nim <= rata kiri dengan lebar 10 karakter
    {"NAMA":<12} artinya:
    tampilkan nama <= rata kiri dengan lebar 12 karakter
    {"NILAI":>5} artinya:
    tampilkan nilai => rata kanan dengan lebar 5 karakter
    '''
    for nim in sorted(data_dict.keys()):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim:10} {nama:<12} {nilai:>5}")

#memanggil fungsi menampilkan data
#tampilkan_data_mahasiswa(buka_data)

#===============================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan dasar 3 : Membuat fungsi cari data
#===============================================
def cari_data(data_dict):
    #mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukkan NIM yang dicari : ").strip()
    if nim_cari in data_dict:
        nama=data_dict[nim_cari]["nama"]
        nilai=data_dict[nim_cari]["nilai"]

        print("\n========Data Mahasiswa Ditemukan========")
        print(f"NIM  : {nim_cari}")
        print(f"NAMA : {nama}")
        print(f"NILAI: {nilai}")
    else:
        print("\nData tidak ditemukan")

#memanggil fungsi cari data
#cari_data(buka_data)


#===============================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan dasar 4 : Membuat statistik nilai
#===============================================
def update_nilai(data_dict):
    nim=input("Masukkan NIM yang akan diupdate nilainya : ").strip()
    
    if nim not in data_dict:
        print("Data tidak ditemukan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (1-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return

    if nilai_baru <1 or nilai_baru >100:
        print("Nilai harus antara 1-100. Update dibatalkan")
        return
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
#Eksekusi update nilai
#update_nilai(buka_data)

#===============================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan dasar 5 : Membuat fungsi menyimpan perubahan data
#===============================================
def simpan_data(nama_file,data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in data_dict:
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#memanggil fungsi simpan data
#simpan_data(nama_file,buka_data)

#===============================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan dasar 6 : Membuat menu program
#===============================================
def main():
    #Menjalankan fungsi load data
    buka_data = baca_data_mahasiswa(nama_file)
while True:
    print("\n======= Menu Data Mahasiswa =======")
    print("1. Tampilkan Data Mahasiswa")
    print("2. Cari Data Mahasiswa")
    print("3. Update Nilai Mahasiswa")
    print("4. Simpan Perubahan Data")
    print("0. Keluar Program")

    pilihan = input("Pilih menu : ").strip()

    if pilihan == "1":
        tampilkan_data_mahasiswa(buka_data)
    elif pilihan == "2":
        cari_data(buka_data)
    elif pilihan == "3":
        update_nilai(buka_data)
    elif pilihan == "4":
        simpan_data(nama_file,buka_data)
        print("Simpan data berhasil.")
    elif pilihan == "0":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()