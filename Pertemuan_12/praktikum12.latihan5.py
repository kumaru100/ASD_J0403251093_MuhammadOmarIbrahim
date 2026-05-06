# ==========================================================
# Tugas: Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# Nama : Muhammad Omar Ibrahim
# Nim: J0403251093
# ==========================================================

import heapq  # modul untuk priority queue (min-heap)

# Representasi graph berbobot antar kota
# Bobot menunjukkan jarak/waktu tempuh antar kota
graph = {
    'Bogor':   {'Jakarta': 5, 'Depok': 2},  # Bogor ke Jakarta (5), Bogor ke Depok (2)
    'Depok':   {'Jakarta': 2, 'Bandung': 6}, # Depok ke Jakarta (2), Depok ke Bandung (6)
    'Jakarta': {'Bandung': 7},               # Jakarta ke Bandung (7)
    'Bandung': {}                            # Bandung tidak punya tetangga (node tujuan)
}

def dijkstra(graph, start):
    """
    Fungsi mencari jarak terpendek dari node start
    ke semua node lain menggunakan algoritma Dijkstra.
    """
    # Inisialisasi semua jarak dengan tak hingga karena belum diketahui
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue menyimpan (jarak, node), diproses dari jarak terkecil
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak ini sudah tidak relevan
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

    return distances  # kembalikan dict jarak terpendek ke semua node

# Tentukan node awal
start_node = 'Bogor'

# Jalankan algoritma Dijkstra dari node awal
hasil = dijkstra(graph, start_node)

# Tampilkan jarak terpendek dari node awal ke semua node
print(f"Jarak terpendek dari {start_node}:")
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")


# Pertanyaan Analisis: 
# 1. Node awal yang digunakan apa? 
# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
# 3. Node mana yang memiliki jarak paling besar dari node awal? 
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat. 


# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor
# 2. Node dengan jarak paling kecil dari Bogor adalah Depok (jarak = 2)
# 3. Node dengan jarak paling besar dari Bogor adalah Bandung (jarak = 8)
# 4. Dijkstra dimulai dari Bogor (jarak 0), lalu memilih tetangga
#    dengan jarak terkecil terlebih dahulu menggunakan priority queue.
#    Pertama Depok (2) diproses, lalu dari Depok ditemukan Jakarta (2+2=4)
#    lebih kecil dari jalur langsung Bogor->Jakarta (5), sehingga diperbarui.
#    Dari Depok juga ditemukan Bandung (2+6=8). Proses berlanjut sampai
#    semua node mendapat jarak terpendek yang optimal.