# ========================================================== 
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# Nama : Muhammad Omar Ibrahim
# Nim: J0403251093
# ========================================================== 
import heapq 
# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
'Perpustakaan': {'Lab': 3}, 
'Kantin': {'Lab': 4, 'Aula': 7}, 
'Lab': {'Aula': 1}, 
'Aula': {} 
} 
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances 
hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
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