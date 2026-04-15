#===================================
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
#Latihan 1: Membuat Node
#===================================

class Node:
    def __init__(self,data):
        self.data = data      # Isi node
        self.left = None      # Child kiri
        self.right = None     # Child kanan
#Membuat root

root = Node('A')          # Root tree

#Menampilkan isi node
print("Data pada root", root.data)  # Tampilkan data root

# Cara kerja: class Node menyimpan data dan dua anak, lalu root dibuat dengan isi 'A'.
# Program ini hanya menampilkan data pada root sebagai contoh node paling dasar.
