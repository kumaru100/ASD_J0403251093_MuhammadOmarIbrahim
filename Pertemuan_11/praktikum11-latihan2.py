graph = { 
'A': ['B', 'C'], 
'B': ['D', 'E'], 
'C': ['F'], 
'D': [], 
'E': [], 
'F': [] 
} 

def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 

    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 
visited = set() 
print("DFS dari A:") 
dfs(graph, 'A', visited)

#Pertanyaan Analisis 
#1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
#2. Apa yang terjadi jika urutan neighbor diubah?  
#3. Bandingkan hasil DFS dengan BFS pada graph yang sama. 

#Jawaban:
#1. DFS masuk ke node terdalam terlebih dahulu karena:
#   - DFS menggunakan pendekatan "telusuri sampai buntu, baru mundur"
#   - Setiap kali menemukan neighbor, langsung masuk ke node tersebut (rekursi)
#   - Tidak berhenti sampai tidak ada neighbor lagi, baru mencoba branch lain

#2. Jika urutan neighbor diubah:
#   - Urutan kunjungan node akan berubah (karena urutan neighbor berbeda)
#   - Tapi semua node tetap dikunjungi (selama graph terhubung)
#   - Contoh: jika B didahulukan sebelum C, maka pohon D-E akan dieksplor lebih dulu

#3. Perbandingan DFS vs BFS pada graph yang sama:
#   - BFS: Rumah → Sekolah, Toko → Perpustakaan, Pasar (level demi level)
#   - DFS: Rumah → Sekolah → Perpustakaan → (kembali) → Toko → Pasar
#   - BFS lebih cocok untuk jalur terdekat, DFS lebih cocok untuk eksplorasi mendalam