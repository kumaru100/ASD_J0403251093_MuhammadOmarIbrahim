class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Fungsi untuk menambah elemen di akhir (append)
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # --- FUNGSI REVERSE (LATIHAN 5) ---
    def reverse(self):
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next  # 1. Simpan node selanjutnya agar tidak hilang
            current.next = prev       # 2. Balikkan pointer ke node sebelumnya
            prev = current            # 3. Geser 'prev' maju ke 'current'
            current = next_node       # 4. Geser 'current' maju ke 'next_node'
            
        self.head = prev  # Update head ke node terakhir (yang sekarang jadi pertama)

    # Fungsi untuk mencetak list sesuai format contoh
    def print_list(self):
        temp = self.head
        if temp is None:
            print("null")
            return
        while temp:
            print(f"{temp.data}", end=" -> ")
            temp = temp.next
        print("null")

# --- MENJALANKAN PROGRAM SESUAI CONTOH ---
if __name__ == "__main__":
    llist = LinkedList()

    # Input User
    try:
        raw_input = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")
        if raw_input.strip(): # Cek jika input tidak kosong
            elements = [int(x.strip()) for x in raw_input.split(',')]
            for el in elements:
                llist.append(el)
        
        # Tampilan Sebelum
        print("Linked List sebelum dibalik: ", end="")
        llist.print_list()

        # Proses Pembalikan
        llist.reverse()

        # Tampilan Sesudah
        print("Linked List setelah dibalik: ", end="")
        llist.print_list()

    except ValueError:
        print("Input error: Pastikan Anda memasukkan angka yang dipisahkan koma.")

        #tes