#=================================================
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
# Latihan 6: Strutur Organisasi Perusahaan
#=================================================
class Node:
    def __init__(self,data):
        self.data = data      # Isi node
        self.left = None      # Child kiri
        self.right = None     # Child kanan

#Fungsi pre order traversal
def preorder(node):
    if node is not None:
        print(node.data)      # Tampil data node
        preorder(node.left)   # Lanjut kiri
        preorder(node.right)  # Lanjut kanan

#Membuat tree struktur organisasi
root = Node("Direktur")   # Pimpinan tertinggi

#Child level 1
root.left = Node("Manager A")   # Cabang kiri
root.right = Node("Manager B")  # Cabang kanan

#Child level 2
root.left.left = Node("Staff 1")   # Staff bawah A
root.left.right = Node("Staff 2")  # Staff bawah A

root.right.left = Node("Staff 3")  # Staff bawah B


#Menjalankan Traversal Preorder
print("Struktur Organisasi (preorder):")  # Judul hasil
preorder(root)                              # Tampilkan tree

# Cara kerja: struktur organisasi digambar sebagai tree, lalu preorder menampilkan pimpinan dulu.
# Setelah itu program masuk ke cabang manager dan staff dari kiri ke kanan.