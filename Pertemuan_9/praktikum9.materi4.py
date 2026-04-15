#=================================================
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
# Latihan 4: Membuat binary search tree
#=================================================
class Node:
    def __init__(self,data):
        self.data = data      # Isi node
        self.left = None      # Child kiri
        self.right = None     # Child kanan

#Membuat fungsi inorder : left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)          # Kunjungi kiri
        print(node.data, end=" ")  # Kunjungi node
        inorder(node.right)         # Kunjungi kanan

#Membuat tree
root = Node('A')          # Root tree

#membuat child level 1
root.left = Node('B')     # Anak kiri root
root.right = Node('C')    # Anak kanan root

#membuat child level 2
root.left.left = Node('D')   # Anak kiri B
root.left.right = Node('E')  # Anak kanan B


print("Hasil tranversal inorder: ")  # Judul hasil
inorder(root)                         # Jalankan inorder

#Penjelasan:
#1. Baca cabang kiri terlebih dahulu.
#2. Lalu baca node sekarang.
#3. Terakhir baca cabang kanan.

# Cara kerja: inorder menelusuri subtree kiri, lalu node, lalu subtree kanan secara rekursif.
# Urutan tampilnya berguna untuk melihat data sesuai posisi kiri ke kanan pada tree.