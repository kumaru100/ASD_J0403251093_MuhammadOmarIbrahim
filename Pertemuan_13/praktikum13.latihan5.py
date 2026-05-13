# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Program Minimum Spanning Tree menggunakan Algoritma Kruskal
# Kasus 1: Jaringan Jalan Antar Kota
# ==========================================================

# Representasi weighted graph dalam bentuk daftar edge.
# Format edge: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil.
# Dalam Kruskal, edge dengan bobot terkecil diproses lebih dulu.
edges.sort()

# mst digunakan untuk menyimpan edge yang terpilih.
mst = []

# total_weight digunakan untuk menghitung total bobot MST.
total_weight = 0

# connected digunakan untuk menyimpan node/kota yang sudah terhubung.
connected = set()

# Memproses setiap edge dari bobot terkecil ke terbesar.
for weight, u, v in edges:
    # Edge dipilih jika salah satu kota belum terhubung.
    # Tujuannya agar tidak membentuk cycle sederhana.
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# Menampilkan edge-edge yang masuk ke MST.
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot minimum.
print("Total bobot minimum =", total_weight)


# ==========================================================
# Pertanyaan Analisis:
# ==========================================================

# Jawaban Analisis:
# 1. Kasus yang dipilih adalah Kasus 1, yaitu jaringan jalan
# antar kota yang menghubungkan Bogor, Jakarta, Depok,
# dan Bandung.

# 2. Algoritma yang digunakan adalah algoritma Kruskal.
# Algoritma ini bekerja dengan cara mengurutkan semua edge
# berdasarkan bobot terkecil, lalu memilih edge yang tidak
# membentuk cycle.

# 3. Edge yang dipilih dalam MST adalah:
# Bogor - Depok = 2
# Depok - Jakarta = 3
# Depok - Bandung = 4

# 4. Total bobot MST adalah:
# 2 + 3 + 4 = 9

# 5. Edge Bogor - Jakarta tidak dipilih karena setelah Bogor,
# Depok, dan Jakarta sudah terhubung, edge tersebut akan
# membentuk cycle. Edge Jakarta - Bandung juga tidak dipilih
# karena bobotnya lebih besar dibandingkan Depok - Bandung.