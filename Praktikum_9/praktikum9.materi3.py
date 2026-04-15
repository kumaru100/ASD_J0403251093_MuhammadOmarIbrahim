#=================================================
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
# Latihan 2: Membuat binary search tree
#=================================================

#Class Node adalah unit dasar pada tree
class Node:
    def __init__(self,data):
        self.data = data      # Isi node
        self.left = None      # Child kiri
        self.right = None     # Child kanan

#Fungsi pre order traversal
def preorder(node):
    if node is not None:
        print(node.data, end=" ")  # Kunjungi node
        preorder(node.left)         # Lanjut kiri
        preorder(node.right)        # Lanjut kanan


#Membuat tree
root = Node('A')          # Root tree

#membuat child level 1
root.left = Node('B')     # Anak kiri root
root.right = Node('C')    # Anak kanan root

#membuat child level 2
root.left.left = Node('D')   # Anak kiri B
root.left.right = Node('E')   # Anak kanan B


#Menjalankan tranversal preorder
print("Hasil tranversal preorder: ")  # Judul hasil
preorder(root)                         # Jalankan preorder

#Penjelasan:
#1. Baca node sekarang dulu.
#2. Lanjut ke cabang kiri.
#3. Terakhir ke cabang kanan.

# Cara kerja: preorder selalu memproses node saat ini lebih dulu, lalu rekursif ke kiri dan kanan.
# Hasilnya urutan kunjungan mengikuti pola root -> kiri -> kanan.