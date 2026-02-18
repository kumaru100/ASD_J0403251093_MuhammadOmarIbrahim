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
        