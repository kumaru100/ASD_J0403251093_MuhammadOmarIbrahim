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

 def enqueue(self, no, nama, servis):
 # TODO: Tambahkan data ke antrian
 pass

 def dequeue(self):
 # TODO: Layani pelanggan terdepan
 pass

 def tampilkan(self):
 # TODO: Tampilkan seluruh antrian
 pass


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
 q.tampilkan()

 elif pilih == "4":
 break

 else:
 print("Pilihan tidak valid")

if __name__ == "__main__":
 main()
