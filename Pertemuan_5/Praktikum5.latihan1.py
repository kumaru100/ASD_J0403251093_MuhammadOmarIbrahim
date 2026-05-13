# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Base case (kondisi berhenti)
    # Jika pangkat = 0, maka hasilnya selalu 1
    # (karena bilangan apapun berpangkat 0 = 1)
    if n == 0:
        return 1
    
    # Recursive case (pemanggilan fungsi dirinya sendiri)
    # a^n = a * a^(n-1)
    # Fungsi akan terus memanggil dirinya
    # dengan nilai n yang dikurangi 1
    return a * pangkat(a, n - 1)

# Pemanggilan fungsi
print(pangkat(2, 4))  # Output: 16