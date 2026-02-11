class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Fungsi untuk menambah elemen di akhir (agar sesuai urutan input)
    def append(self, new_data):
        new_node = Node(new_data)
        
        # Jika list kosong, node baru menjadi head
        if self.head is None:
            self.head = new_node
            return
            
        # Jika tidak, telusuri sampai node terakhir
        last = self.head
        while last.next:
            last = last.next
            
        # Hubungkan node terakhir dengan node baru
        last.next = new_node
        new_node.prev = last

    # --- FUNGSI PENCARIAN (LATIHAN 3) ---
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True # Elemen ditemukan
            current = current.next
        return False # Elemen tidak ditemukan setelah loop selesai

    # Fungsi bantu untuk menampilkan list
    def print_list(self):
        node = self.head
        print("Isi List: ", end="")
        while node:
            print(f"{node.data}", end=" <-> " if node.next else "")
            node = node.next
        print()

# --- BAGIAN INTERAKTIF SESUAI CONTOH ---
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # 1. Input elemen (Mensimulasikan input user: 2, 6, 9, 14, 20)
    raw_input = input("Masukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ")
    # Mengubah string input "2, 6, 9..." menjadi list integer
    elements = [int(x.strip()) for x in raw_input.split(',')]
    
    for el in elements:
        dll.append(el)

    # 2. Input elemen yang dicari
    cari = int(input("Masukkan elemen yang ingin dicari: "))

    # 3. Eksekusi pencarian
    ditemukan = dll.search(cari)

    # 4. Tampilkan Hasil
    if ditemukan:
        print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
    else:
        print(f"Elemen {cari} TIDAK ditemukan dalam Doubly Linked List.")
        #tes