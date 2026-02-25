#=================================================
#Nama = Muhammad Omar Ibrahim
#NIM = J0403251093
#Kelas = TPL B1 
#=================================================

#=================================================
# Materi Rekursif : Call Stack
# Tracing Bilangan (masuk-keluar) 
# Input 3
# Masuk 1 - 2 - 3 
# Keluar 3 - 2 - 1
#=================================================

def hitung(n):

    #Base case
    if n==0:
        print("Selesai")
        return

    print("Masuk : ", n)
    hitung(n-1) #recursive case
    print("Keluar : ", n)


print("=========Program Tracing===========")
hitung(int(input("Masukkan angka yang mau di tresing : ")))
