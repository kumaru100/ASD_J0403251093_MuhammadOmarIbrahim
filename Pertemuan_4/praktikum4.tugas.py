# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

# Kelas Node: Menyimpan data satu pelanggan dalam antrian
class Node:
    def __init__(self, no, nama, servis):
        # no: nomor antrian
        # nama: nama pelanggan
        # servis: jenis servis yang diinginkan
        # next: pointer ke node berikutnya
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None

# Kelas QueueBengkel: Mengimplementasikan antrian (FIFO - First In First Out) untuk bengkel
class QueueBengkel:
    def __init__(self):
        # front: pointer ke pelanggan paling depan (yang akan dilayani pertama)
        # rear: pointer ke pelanggan paling belakang (pelanggan terakhir yang masuk)
        self.front = None
        self.rear = None

    def is_empty(self):
        # Cek apakah antrian kosong
        # Jika front None berarti tidak ada pelanggan dalam antrian
        return self.front is None

    def enqueue(self, no, nama, servis):
        # Menambahkan pelanggan baru ke belakang antrian
        # Buat node baru dengan data pelanggan
        nodeBaru = Node(no, nama, servis)
        
        # Jika antrian kosong, node baru menjadi front dan rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear  = nodeBaru
            print(f"Pelanggan {nama} ditambahkan ke antrian")
            return
        
        # Jika antrian tidak kosong, tambahkan node baru di belakang
        # Hubungkan node rear lama dengan node baru
        self.rear.next = nodeBaru
        # Update rear ke node baru
        self.rear = nodeBaru
        print(f"Pelanggan {nama} ditambahkan ke antrian")
    

    def dequeue(self):
        # Melayani pelanggan terdepan (yang pertama masuk)
        # Cek apakah ada pelanggan dalam antrian
        if self.is_empty():
            print("Antrian Kosong, Tidak ada motor yang diperbaiki !")
            return None
        
        # Simpan data pelanggan yang akan dilayani ke variabel
        nodeDilayani = self.front
        
        # Geser pointer front ke node berikutnya
        self.front = self.front.next
        
        # Jika front menjadi None (artinya semua pelanggan sudah dilayani)
        # maka rear juga harus None agar antrian benar-benar kosong
        if self.front is None:
            self.rear = None
        
        # Tampilkan data pelanggan yang baru saja dilayani
        print(f"Pelanggan {nodeDilayani.nama} sedang dilayani (Servis: {nodeDilayani.servis})")
        
        return nodeDilayani

    def tampilkan(self):
        # Menampilkan seluruh antrian dari front (paling depan) hingga rear (paling belakang)
        print("Daftar Antrian Bengkel Motor (Front -> Rear) : ")
        
        # Mulai dari node paling depan (front)
        current = self.front
        no = 1
        
        # Loop melalui semua node dalam antrian
        while current is not None:
            # Tampilkan data setiap pelanggan yang ada dalam antrian
            print(f"{no}. No Antrian: {current.no}, Nama: {current.nama}, Servis: {current.servis}")
            # Pindah ke node berikutnya
            current = current.next
            no += 1


def main():
    # Buat instance antrian bengkel
    q = QueueBengkel()
    
    # Loop menu utama
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        # Menu 1: Tambah pelanggan baru ke antrian
        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)

        # Menu 2: Layani pelanggan paling depan dalam antrian
        elif pilih == "2":
            q.dequeue()
  
        # Menu 3: Tampilkan semua pelanggan yang ada dalam antrian
        elif pilih == "3":
            print("\n")
            q.tampilkan()

        # Menu 4: Keluar dari program
        elif pilih == "4":
            print("Terima kasih telah menggunakan Sistem Antrian Bengkel!")
            break

        # Jika pilihan tidak sesuai dengan menu yang ada
        else:
            print("Pilihan tidak valid")

# Jalankan program utama ketika file ini dieksekusi langsung
if __name__ == "__main__":
    main()
