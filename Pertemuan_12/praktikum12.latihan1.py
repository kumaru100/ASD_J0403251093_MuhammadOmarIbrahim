# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# Nama : Muhammad Omar Ibrahim
# Nim: J0403251093
# ========================================================== 

# Representasi weighted graph menggunakan dictionary bersarang 
# Setiap node adalah key dengan value berupa dict yang berisi node tetangga dan bobot edge-nya
graph = { 
    'A': {'B': 4, 'C': 2},  # Dari A bisa ke B (bobot 4) atau ke C (bobot 2)
    'B': {'D': 5},          # Dari B bisa ke D (bobot 5)
    'C': {'D': 1},          # Dari C bisa ke D (bobot 1)
    'D': {}                 # D adalah node tujuan, tidak ada edge keluar
} 

# Menghitung dua kemungkinan jalur dari A ke D 
# Jalur 1: A -> B -> D
jalur_1 = graph['A']['B'] + graph['B']['D']  # 4 + 5 = 9
# Jalur 2: A -> C -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # 2 + 1 = 3

# Menampilkan total bobot untuk masing-masing jalur
print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

# Membandingkan dan menentukan jalur terpendek
if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D") 

# Jawaban Analisis: 
# 1. Berapa total bobot jalur A -> B -> D? 
# 2. Berapa total bobot jalur A -> C -> D? 
# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang 
#paling sedikit? 


# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D = 4 + 5 = 9
# 2. Total bobot jalur A -> C -> D = 2 + 1 = 3
# 3. Jalur terpendek: A -> C -> D (bobot 3 < 9)
# 4. Karena jalur terpendek ditentukan dari total bobot, bukan jumlah edge.
#    Edge sedikit belum tentu lebih murah jika bobotnya besar.