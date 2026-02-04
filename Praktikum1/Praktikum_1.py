#===============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan dasar 1 : Membaca seluruh isi file
#===============================================


#membuka file dalam mode read("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()

print(isi_file)
print("===Hasil Read===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karater", len(isi_file))
print("Jumlah Baris", isi_file.count("\n")+1)

print("===Membaca per Baris===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris +=1 
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)

#===============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan dasar 2 : Parsing baris menjadi kolom data
#===============================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",")
        print("NIM :", nim, "|NAMA :", nama, "|NILAI :", nilai)


#===============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan dasar 3: Membaca File dan Menyimpan ke List
#===============================================
#List untuk menampung
data_list = []


with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",")
        #simpan sebagai list [nim, nama, nilai]
        data_list.append([nim,nama,int(nilai)])

print("=== Data Mahasiswa dalam List ===")
print(data_list)

print("=== Jumlah Record dalam List ===")
print("Jumlah Record :", len(data_list))

print("=== Menampilkan Data Record Tertentu ===")
print("Contoh Record Pertama :", data_list[0])

#===============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan dasar 4: Membaca File dan Menyimpan ke Dictionary
#===============================================

data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",")

        #simpan data mahasiswa ke dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai),
        }
print("=== Data Mahasiswa dalam Dictionary")
print(data_dict)