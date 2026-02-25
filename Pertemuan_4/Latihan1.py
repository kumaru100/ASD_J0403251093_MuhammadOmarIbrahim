#================================================
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
#================================================

#================================================
# Implementasi Dasar : Queue berbasis linked list
#================================================

class Node:
    def __init__(self, data): #konstruktor untuk inisialisasi node
        self.data = data #menyimpan nilai data
        self.next = None #pointer ke node berikutnya

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        #Menambah data di belakang (tail)
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #Rear pindah ke node baru
        self.rear.next = nodeBaru
        self.rear = nodeBaru
        
    def dequeue(self):
        #menghapus data dari depan (head)

        #1)peek/lihat data paling depan
        data_terhapus = self.front.data

        #2)geser front ke node berikutnya
        self.front = self.front.next

        #3)Jika setelah geser front menjadi None, berarti queue kosong
        #maka rear juga None
        if self.front is None:
            self.rear = None

    
    def tampilkan(self):
        #Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front", end=" -> ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Rear di node terakhir")

#Instantiasi objek class queuell
q=QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()