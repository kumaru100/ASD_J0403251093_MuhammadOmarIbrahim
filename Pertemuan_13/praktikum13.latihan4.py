# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree

# Program ini menggunakan algoritma Kruskal sederhana
# untuk mencari Minimum Spanning Tree (MST).

# Daftar edge: (bobot, node1, node2)
# Bobot menunjukkan nilai/jarak antar node.
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
# agar edge dengan bobot paling kecil diproses lebih dulu.
edges.sort()

# mst digunakan untuk menyimpan edge yang terpilih
# sebagai bagian dari Minimum Spanning Tree.
mst = []

# total_weight digunakan untuk menghitung total bobot MST.
total_weight = 0

# connected digunakan untuk menyimpan node yang sudah terhubung.
connected = set()

# Melakukan pengecekan setiap edge yang sudah diurutkan.
for weight, u, v in edges:
    # Edge dipilih jika salah satu node belum terhubung.
    # Tujuannya agar tidak membentuk cycle sederhana.
    if u not in connected or v not in connected:
        # Menambahkan edge ke dalam MST.
        mst.append((u, v, weight))

        # Menambahkan bobot edge ke total bobot MST.
        total_weight += weight

        # Menandai node u dan v sebagai node yang sudah terhubung.
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST.
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot dari semua edge yang terpilih.
print("Total bobot =", total_weight)


# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
# 2. Edge mana saja yang dipilih?
# 3. Berapa total biaya minimum?
# 4. Mengapa MST cocok digunakan pada kasus ini?

# Jawaban Analisis:
# 1. Algoritma yang digunakan adalah Kruskal.
# 2. Edge yang dipilih adalah (1, 'C', 'D'), (2, 'A', 'C'), dan (3, 'B', 'D').
# 3. Total biaya minimum adalah 6 (1 + 2 + 3).
# 4. MST cocok digunakan pada kasus ini karena kita ingin menghubungkan semua node dengan biaya minimum tanpa membentuk cycle, sehingga MST memberikan solusi optimal untuk masalah ini.