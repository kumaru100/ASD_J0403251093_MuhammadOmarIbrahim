# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum (Rekursi pada List)
# ==========================================================

def cari_maks(data, index=0):
    
    # Base case (kondisi berhenti)
    # Jika index sudah berada di elemen terakhir list,
    # maka langsung kembalikan nilai elemen tersebut
    # karena tidak ada lagi yang bisa dibandingkan.
    if index == len(data) - 1:
        return data[index]
    
    # Recursive case
    # Fungsi memanggil dirinya sendiri untuk mencari
    # nilai maksimum dari sisa list (index + 1 sampai akhir)
    maks_sisa = cari_maks(data, index + 1)
    
    # Setelah mendapatkan maksimum dari sisa list,
    # bandingkan dengan elemen saat ini (data[index])
    if data[index] > maks_sisa:
        return data[index]   # Jika elemen sekarang lebih besar
    else:
        return maks_sisa     # Jika maksimum sisa lebih besar


# Data yang akan dicari nilai maksimumnya
angka = [3, 7, 2, 9, 5]

# Pemanggilan fungsi
print("Nilai maksimum:", cari_maks(angka))