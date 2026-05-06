# ==========================================================
# Latihan 2: Implementasi Dijkstra
# Nama : Muhammad Omar Ibrahim
# Nim: J0403251093
# ==========================================================
import heapq  # modul untuk priority queue (min-heap)

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},  # A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},           # B terhubung ke D (bobot 5)
    'C': {'D': 1},           # C terhubung ke D (bobot 1)
    'D': {}                  # D tidak punya tetangga (node tujuan)
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Inisialisasi semua jarak dengan tak hingga karena belum diketahui
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke dirinya sendiri selalu 0
    distances[start] = 0

    # Priority queue menyimpan (jarak, node), diurutkan dari jarak terkecil
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak ini sudah tidak relevan (ada yang lebih kecil sebelumnya)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung total jarak ke tetangga melalui node saat ini
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil, perbarui dan masukkan ke queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances  # kembalikan dict berisi jarak terpendek ke semua node

# Jalankan Dijkstra mulai dari node 'A'
hasil = dijkstra(graph, 'A')

# Tampilkan hasil jarak terpendek dari A ke semua node
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Pertanyaan Analisis: 
# 1. Berapa jarak terpendek dari A ke B? 
# 2. Berapa jarak terpendek dari A ke C? 
# 3. Berapa jarak terpendek dari A ke D? 
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?


# Jawaban Analisis:
# 1. Jarak terpendek A ke B = 4
# 2. Jarak terpendek A ke C = 2
# 3. Jarak terpendek A ke D = 3 (lewat C: 2+1)
# 4. Karena A->C->D = 2+1 = 3, lebih kecil dari A->B->D = 4+5 = 9
# 5. Priority queue memastikan node dengan jarak terkecil diproses duluan
# 6. Bobot negatif bisa membuat jarak terus berkurang tak terbatas,
#    sehingga algoritma tidak bisa menemukan jarak optimal yang benar