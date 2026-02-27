# ==========================================================
# Latihan 4: Kombinasi Huruf (Backtracking Dasar)
# ==========================================================

def kombinasi(n, hasil=""):
    
    # Base case (kondisi berhenti)
    # Jika panjang string 'hasil' sudah sama dengan n,
    # maka kombinasi sudah lengkap
    if len(hasil) == n:
        print(hasil)   # Cetak kombinasi
        return         # Hentikan cabang ini
    
    # Recursive case (choose & explore)
    
    # Pilihan 1: tambahkan huruf "A"
    kombinasi(n, hasil + "A")
    
    # Pilihan 2: tambahkan huruf "B"
    kombinasi(n, hasil + "B")


# Memulai kombinasi dengan panjang 2
kombinasi(2)