#=================================================
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
#=================================================


graph ={
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

for node in graph:
    print(node, "->", graph[node])
