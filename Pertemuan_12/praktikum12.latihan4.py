# ========================================================== 
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# Nama : Muhammad Omar Ibrahim
# Nim: J0403251093
# ========================================================== 
import heapq  # Library untuk priority queue (heap)

# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
# Struktur: {node: {tetangga: jarak, ...}, ...}
graph = { 
'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
'Perpustakaan': {'Lab': 3}, 
'Kantin': {'Lab': 4, 'Aula': 7}, 
'Lab': {'Aula': 1}, 
'Aula': {} 
} 
def dijkstra(graph, start):
    # Inisialisasi jarak semua node ke infinity, kecuali start node = 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue untuk menyimpan (jarak, node)
    # Digunakan untuk memilih node dengan jarak minimum berikutnya
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip jika kita sudah menemukan jalur lebih pendek ke node ini
        if current_distance > distances[current_node]:
            continue
        
        # Cek semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru melalui current_node
            distance = current_distance + weight
            
            # Jika jarak baru lebih pendek, update jarak dan tambah ke priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Kembalikan dictionary dengan jarak terpendek ke semua node
    return distances 
# Jalankan algoritma Dijkstra dari node 'Gerbang'
hasil = dijkstra(graph, 'Gerbang')

# Tampilkan hasil jarak terpendek dari Gerbang ke semua lokasi
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    # Cetak setiap lokasi dengan jarak terdekatnya
    print(lokasi, "=", jarak, "menit")


# Pertanyaan Analisis: 
# 1. Lokasi mana yang paling dekat dari Gerbang? 
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? 
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini? 

# Jawaban Analisis:
# 1. Lokasi paling dekat dari Gerbang adalah Kantin (2 menit)
# 2. Waktu tempuh terpendek Gerbang ke Aula = 7 menit
#    (Gerbang -> Kantin -> Lab -> Aula = 2+4+1)
# 3. Tidak selalu. Contoh: Gerbang -> Aula langsung tidak ada,
#    jalur terpendek justru lewat beberapa node dengan total bobot lebih kecil
# 4. Karena semua bobot (waktu tempuh) bernilai positif,
#    sehingga Dijkstra bisa bekerja optimal dan efisien