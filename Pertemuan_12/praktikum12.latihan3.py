# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# Nama : Muhammad Omar Ibrahim
# Nim: J0403251093
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},  # A ke B (bobot 5), A ke C (bobot 4)
    'B': {},                  # B tidak punya tetangga
    'C': {'B': -2}            # C ke B (bobot negatif -2)
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Inisialisasi semua jarak dengan tak hingga karena belum diketahui
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke dirinya sendiri selalu 0
    distances[start] = 0

    # Relaksasi dilakukan sebanyak jumlah node - 1 kali
    # agar semua kemungkinan jalur terpendek sempat diperiksa
    for _ in range(len(graph) - 1):
        # Periksa setiap edge di seluruh graph
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika node sudah terjangkau dan ditemukan jarak lebih kecil,
                # perbarui jarak ke neighbor
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances  # kembalikan dict jarak terpendek ke semua node

# Jalankan Bellman-Ford mulai dari node 'A'
hasil = bellman_ford(graph, 'A')

# Tampilkan hasil jarak terpendek dari A ke semua node
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis: 
# 1. Berapa bobot langsung dari A ke B? 
# 2. Berapa total bobot jalur A -> C -> B? 
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? 
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
# 5. Apa yang dimaksud dengan proses relaksasi edge? 
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra? 

# Jawaban Analisis:
# 1. Bobot langsung A ke B = 5
# 2. Total bobot A -> C -> B = 4 + (-2) = 2
# 3. Jalur A -> C -> B lebih kecil (2 < 5)
# 4. Karena Bellman-Ford memeriksa semua edge berulang kali sehingga
#    bobot negatif tetap bisa dihitung dengan benar
# 5. Relaksasi adalah proses memperbarui jarak ke suatu node jika
#    ditemukan jalur yang lebih pendek dari jalur sebelumnya
# 6. Dijkstra lebih cepat tapi tidak bisa menangani bobot negatif,
#    Bellman-Ford lebih lambat tapi bisa menangani bobot negatif