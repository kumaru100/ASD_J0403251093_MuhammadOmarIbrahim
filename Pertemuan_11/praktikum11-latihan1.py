# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093

graph = { 
'Rumah': ['Sekolah', 'Toko'], 
'Sekolah': ['Perpustakaan'], 
'Toko': ['Pasar'], 
'Perpustakaan': [], 
'Pasar': [] 
} 

from collections import deque 
def bfs(graph, start): 
    visited = set() 
    queue = deque([start]) 
    visited.add(start) 
    while queue: 
        node = queue.popleft() 
        print(node, end=" ") 
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 

print("BFS dari Rumah:") 
bfs(graph, 'Rumah') 

#..................................... 
#Pertanyaan Analisis 
#1. Node mana yang dikunjungi pertama?  
#2. Mengapa BFS cocok untuk mencari jalur terdekat?  
#3. Apa perbedaan urutan BFS jika struktur graph diubah? 

#Jawab:
#1. Node yang dikunjungi pertama adalah 'Rumah' karena itu adalah titik awal (start node).
#   BFS selalu dimulai dari node yang kita tentukan sebagai awal pencarian.

#2. BFS cocok untuk mencari jalur terdekat karena:
#   - BFS mengunjungi node berdasarkan tingkat kedalaman/jarak dari node awal
#   - Node yang lebih dekat dengan awal akan dikunjungi lebih dulu
#   - Ini menjamin bahwa jalur pertama yang ditemukan adalah jalur terpendek

#3. Perbedaan urutan BFS jika struktur graph diubah:
#   - Jika menambah/mengurangi edge (koneksi), urutan kunjungan akan berbeda
#   - Jika mengganti node awal, hasilnya akan berbeda
#   - Tapi prinsipnya tetap sama: level demi level dari node awal 