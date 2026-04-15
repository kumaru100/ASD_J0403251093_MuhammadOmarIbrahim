#=================================================
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
# Latihan 2: Membuat Node Tree
#=================================================

#Class Node adalah unit dasar pada tree
class Node:
    def __init__(self,data):
        self.data = data      # Isi node
        self.left = None      # Child kiri
        self.right = None     # Child kanan

#Membuat root
root = Node('A')          # Root tree

#membuat child level 1
root.left = Node('B')     # Anak kiri root
root.right = Node('C')    # Anak kanan root

#membuat child level 2
root.left.left = Node('D')   # Anak kiri dari B
root.left.right = Node('E')  # Anak kanan dari B

#menampilkan isi node
print("Data pada root", root.data)            # Tampil root
print("Data kiri root", root.left.data)       # Tampil kiri root
print("Data kanan root", root.right.data)     # Tampil kanan root
print("Data kiri root kiri", root.left.left.data)    # Tampil node D
print("Data kanan root kiri", root.left.right.data)   # Tampil node E

#pejelasan

# Cara kerja: root dibuat terlebih dahulu, lalu child kiri dan kanan diisi bertingkat.
# Setiap print dipakai untuk mengecek isi node dari atas ke bawah dan dari kiri ke kanan.
