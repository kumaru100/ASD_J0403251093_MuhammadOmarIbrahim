#=================================================
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
# Latihan 5: Membuat binary search tree
#=================================================
class Node:
    def __init__(self,data):
        self.data = data      # Isi node
        self.left = None      # Child kiri
        self.right = None     # Child kanan

#Membuat fungsi inorder : left -> root -> right
def postorder(node):
    if node is not None:
        postorder(node.left)        # Kunjungi kiri
        postorder(node.right)       # Kunjungi kanan
        print(node.data, end=" ")  # Kunjungi node


#Membuat tree
root = Node('A')          # Root tree

#membuat child level 1
root.left = Node('B')     # Anak kiri root
root.right = Node('C')    # Anak kanan root

#membuat child level 2
root.left.left = Node('D')   # Anak kiri B
root.left.right = Node('E')  # Anak kanan B

#Membuat child Level 3
root.left.left.left = Node('F')  # Anak kiri D


print("Hasil tranversal inorder: ")  # Judul hasil
postorder(root)                       # Jalankan postorder

#Penjelasan:
#1. Baca cabang kiri terlebih dahulu.
#2. Lalu baca cabang kanan.
#3. Terakhir baca node sekarang.

# Cara kerja: postorder memproses seluruh anak kiri, lalu anak kanan, baru node induk.
# Pola ini cocok saat data induk baru boleh diproses setelah semua turunannya selesai.
