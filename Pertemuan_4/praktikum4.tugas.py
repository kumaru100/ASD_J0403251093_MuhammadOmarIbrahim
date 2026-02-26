# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None

class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        #Ketika queue kosong maka front = rear = none
        return self.front is None

    def enqueue(self, no, nama, servis):
        # TODO: Tambahkan data ke antrian
        nodeBaru = Node(no, nama, servis)
        # gunakan pemanggilan method agar kondisi dievaluasi dengan benar
        if self.is_empty():
            self.front = nodeBaru
            self.rear  = nodeBaru
            return
        
        self.rear.next = nodeBaru
        self.rear = nodeBaru
    

    def dequeue(self):
 # TODO: Layani pelanggan terdepan
        if self.is_empty():
            print("Antrian Kosong, Tidak ada motor yang diperbaiki !")
            return None
        
                #Lihat data bagian front, simpan di variabel yang akan dihapus
        nodeDilayani = self.front

        #Geser pointer front ke next node
        self.front = self.front.next

        #Jika front menjadi none (data antrian terakhit yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return nodeDilayani

    def tampilkan(self):
 # TODO: Tampilkan seluruh antrian
        print("Daftar Antrian Bengkel Motor (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.no}, {current.nama} = {current.servis}")
            current = current.next
            no += 1


def main():
    q = QueueBengkel()
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()
  
        elif pilih == "3":
            print("\n")
            q.tampilkan()

        elif pilih == "4":
            break

        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
