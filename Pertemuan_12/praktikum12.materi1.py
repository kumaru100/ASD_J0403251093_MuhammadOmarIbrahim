#===============================
# Nama : Muhammad Omar Ibrahim
# Nim: J0403251093
#===============================


# Import heapq untuk priority queue (min-heap)
import heapq 

# Definisikan weighted graph sebagai dictionary bersarang
# Format: {node: {neighbor: bobot_edge, ...}}
graph = { 
    'A': {'B': 4, 'C': 2},  # Dari A ke B bobot 4, ke C bobot 2
    'B': {'D': 5},          # Dari B ke D bobot 5
    'C': {'D': 1},          # Dari C ke D bobot 1
    'D': {}                 # D adalah node tujuan, tidak ada edge keluar
} 

def dijkstra(graph, start): 
    """
    Algoritma Dijkstra: Mencari jarak terpendek dari node start ke semua node lain
    Metode: Greedy algorithm menggunakan priority queue
    """
    # Inisialisasi semua jarak dengan nilai tak hingga (belum dijelajahi)
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari start ke start adalah 0 (titik awal)
    distances[start] = 0 
    
    # Priority queue menyimpan tuple (jarak_dari_start, node)
    # Min-heap memastikan node dengan jarak terkecil diproses duluan
    pq = [(0, start)] 
    
    # Proses sampai semua node yang terjangkau sudah diproses
    while pq: 
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(pq) 
        
        # Periksa semua tetangga (neighbor) dari node saat ini
        for neighbor, weight in graph[current_node].items(): 
            # Hitung jarak baru: jarak saat ini + bobot edge ke neighbor
            distance = current_distance + weight 
            
            # Jika ditemukan jarak yang lebih pendek ke neighbor, perbarui
            if distance < distances[neighbor]: 
                # Update jarak terpendek ke neighbor
                distances[neighbor] = distance 
                # Tambahkan neighbor ke priority queue untuk diproses
                heapq.heappush(pq, (distance, neighbor)) 
    
    # Kembalikan dictionary berisi jarak terpendek dari start ke semua node
    return distances 

# Jalankan algoritma Dijkstra dari node 'A'
hasil = dijkstra(graph, 'A') 

# Tampilkan hasil jarak terpendek dari A ke setiap node
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"A ke {node}: {distance}")