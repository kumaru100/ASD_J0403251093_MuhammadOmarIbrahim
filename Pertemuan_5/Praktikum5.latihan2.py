# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    
    # Base case (kondisi berhenti)
    # Jika n sudah 0, cetak "Selesai"
    # lalu hentikan fungsi dengan return
    if n == 0:
        print("Selesai")
        return
    
    # Bagian ini dijalankan SAAT MASUK ke fungsi
    # sebelum pemanggilan rekursif berikutnya
    print("Masuk:", n)
    
    # Pemanggilan rekursif
    # Fungsi memanggil dirinya sendiri
    # dengan nilai n yang lebih kecil (n - 1)
    countdown(n - 1)
    
    # Bagian ini dijalankan SAAT KELUAR dari fungsi
    # yaitu setelah pemanggilan rekursif selesai
    print("Keluar:", n)


# Memulai proses rekursi
countdown(3)