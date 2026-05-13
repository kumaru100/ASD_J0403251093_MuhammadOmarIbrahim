# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree


import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):
    visited = set([start])
    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
# 2. Edge mana yang dipilih pertama kali?
# 3. Bagaimana Prim menentukan edge berikutnya?
# 4. Berapa total bobot MST yang dihasilkan?
# 5. Apa perbedaan pendekatan Prim dan Kruskal?

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah 'A'.
# 2. Edge yang dipilih pertama kali adalah (2, 'A', 'C') karena memiliki bobot terkecil.
# 3. Edge berikutnya ditentukan dengan memilih edge yang memiliki bobot paling kecil dari semua edge yang
# terhubung dengan vertex yang sudah dikunjungi. Edge tersebut dipilih jika menuju ke vertex yang belum dikunjungi, agar tidak membentuk cycle.
# 4. Total bobot MST yang dihasilkan adalah 6 (2 + 1 + 3).
# 5. Perbedaan Prim dan Kruskal adalah Prim memulai dari satu vertex, lalu memilih edge dengan bobot
# terkecil yang terhubung ke vertex yang sudah dikunjungi.
# Sedangkan Kruskal memilih edge dengan bobot terkecil dari seluruh graph, lalu memasukkannya ke MST selama tidak membentuk cycle.
