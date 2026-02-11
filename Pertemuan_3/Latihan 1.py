class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Menambah node di depan (Head)
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Menghapus node berdasarkan key
    def delete_node(self, key):
        temp = self.head

        # 1. Jika head node memegang key yang dicari
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            print(f"Berhasil menghapus {key}.")
            return

        # 2. Mencari key di sisa list
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # 3. Jika key tidak ditemukan
        if temp is None:
            print(f"Nilai {key} tidak ditemukan dalam list.")
            return

        # 4. Unlink node
        prev.next = temp.next
        temp = None
        print(f"Berhasil menghapus {key}.")

    # Mencetak isi list
    def print_list(self):
        temp = self.head
        if temp is None:
            print(" (List Kosong)")
            return
        print("Isi List saat ini: ", end="")
        while temp:
            print(f" {temp.data} ->", end="")
            temp = temp.next
        print(" None")

# --- BAGIAN UTAMA ---
if __name__ == "__main__":
    llist = LinkedList()

    # --- DATA SUDAH DISEDIAKAN DI SINI ---
    # Anda bisa mengubah angka-angka di dalam kurung siku ini
    angka_bawaan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Memasukkan data ke Linked List
    # Kita reverse agar urutan di layar sama dengan urutan di list angka_bawaan
    for angka in reversed(angka_bawaan):
        llist.push(angka)

    print("=== PROGRAM HAPUS NODE (DATA PRE-DEFINED) ===")
    
    # Langsung masuk ke Loop interaktif
    while True:
        print("\n--------------------------------")
        # 1. Tampilkan kondisi list saat ini
        llist.print_list()
        
        # 2. Cek jika list sudah habis
        if llist.head is None:
            print("\nList sudah kosong. Tidak ada yang bisa dihapus.")
            print("Program berhenti.")
            break

        # 3. Konfirmasi user
        tanya = input("\nApakah Anda ingin menghapus node? (y/n): ").lower()
        if tanya != 'y':
            print("Program selesai. Terima kasih!")
            break
        
        # 4. Proses Input & Hapus
        try:
            key_hapus = int(input("Masukkan angka yang ingin dihapus: "))
            llist.delete_node(key_hapus)
        except ValueError:
            print("❌ Error: Harap masukkan angka bulat saja.")