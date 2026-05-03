graph = {  # representasi graph dengan adjacency list
'A': ['B', 'C'],  # tetangga langsung dari A
'B': ['D', 'E'],  # tetangga langsung dari B
'C': ['F'],  # tetangga langsung dari C
'D': [],  # D tidak memiliki tetangga
'E': [],  # E tidak memiliki tetangga
'F': []  # F tidak memiliki tetangga
} 

def dfs(graph, node, visited): 
    visited.add(node)  # menandai node sebagai sudah dikunjungi
    print(node, end=" ")  # menampilkan node saat ini

    for neighbor in graph[node]:  # iterasi setiap tetangga dari node
        if neighbor not in visited:  # hanya telusuri tetangga yang belum dikunjungi
            dfs(graph, neighbor, visited)  # telusuri lebih dalam secara rekursif
visited = set()  # menyimpan daftar node yang sudah dikunjungi
print("DFS dari A:")  # penanda output traversal DFS
dfs(graph, 'A', visited)  # mulai traversal dari node A

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
