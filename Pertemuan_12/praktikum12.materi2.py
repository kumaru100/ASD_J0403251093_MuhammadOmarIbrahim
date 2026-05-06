#===============================
# Nama : Muhammad Omar Ibrahim
# Nim: J0403251093
#===============================


def bellman_ford(graph, start): 
    """
    Algoritma Bellman-Ford: Mencari jarak terpendek dari node start ke semua node lain
    Keunggulan: Dapat menangani edge dengan bobot negatif
    """
    # Inisialisasi semua jarak dengan nilai tak hingga (belum dijelajahi)
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari start ke start adalah 0 (titik awal)
    distances[start] = 0 
    
    # Lakukan relaksasi (pembaruan jarak) sebanyak (jumlah_node - 1) kali
    # Ini menjamin semua jarak terpendek ditemukan
    for _ in range(len(graph) - 1): 
        # Iterasi melalui setiap node dalam graph
        for node in graph: 
            # Periksa setiap edge (tetangga) dari node saat ini
            for neighbor, weight in graph[node].items(): 
                # Relaksasi: Jika ada jalur lebih pendek ditemukan, perbarui jaraknya
                if distances[node] + weight < distances[neighbor]: 
                    # Update jarak terpendek ke neighbor
                    distances[neighbor] = distances[node] + weight 
    
    # Kembalikan dictionary berisi jarak terpendek dari start ke semua node
    return distances 