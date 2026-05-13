# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph
edges = [
('A', 'B'),
('A', 'C'),
('A', 'D'),
('C', 'D'),
('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
('A', 'C'),
('C', 'D'),
('D', 'B')
]
print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# Pertanyaan Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

# Jawaban Analisis:

# 1. Perbedaan antara graph awal dan spanning tree adalah
# bahwa graph awal dapat memiliki lebih banyak edge dan
# mungkin memiliki cycle, sedangkan spanning tree adalah
# subgraph yang menghubungkan semua vertex tanpa
# membentuk cycle.

# 2. Spanning tree tidak boleh memiliki cycle karena
# tujuan utama dari spanning tree adalah untuk
# menghubungkan semua vertex dengan jumlah edge yang
# minimal. Jika ada cycle, maka ada edge yang tidak
# diperlukan untuk menjaga konektivitas, sehingga
# tidak efisien.

# 3. Jumlah edge spanning tree selalu lebih sedikit
# karena spanning tree hanya mencakup edge yang
# diperlukan untuk menghubungkan semua vertex tanpa loop.