#================================================
# Implementasi Dasar : Node pada Linked List
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
#================================================

# Membuat class Node (Merupakan unit dasar dari linked list)
class Node:
    def __init__(self, data): #konstruktor untuk inisialisasi node
        self.data = data #menyimpan nilai data
        self.next = None #pointer ke node berikutnya
#1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

#3) Menentukan node pertama (head)
head = nodeA

#4) Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data) #Menampilkan data pada node saat ini
    current = current.next #Pindah ke node berikutnya

#================================================
# Implementasi Dasar : Linked List + Insert Awal
#================================================

class LinkedList: #class implementasi stack
    def __init__(self):
        self.head = None #Awalnya kosong


    def insert_awal(self, data): #Konsep Push dalam stack
        #1) Buat node baru
        nodeBaru=Node(data) #Panggil class node
        #2) node baru menunjuk ke head lama
        nodeBaru.next = self.head
        #3)head pindah ke node baru
        self.head = nodeBaru
    
    def hapus_awal(self): #Konsep Pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        self.head = self.head.next  #Menggeser head ke node berikutnya
        print("Data yang dihapus:", data_terhapus)

    def tampilkan(self): #Implementasi traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("======= List Baru =======")
ll = LinkedList() #Instantiasi objek ke class linked list
ll.insert_awal("X") #Insert node dengan data "X"
ll.insert_awal("Y") #Insert node dengan data "Y"
ll.insert_awal("Z") #Insert node dengan data "Z"
ll.tampilkan() #Menampilkan isi linked list
ll.hapus_awal() #Hapus node pertama (Z)
ll.tampilkan() #Menampilkan isi linked list setelah penghapusan
