#=================================================
#Nama = Muhammad Omar Ibrahim
#NIM = J0403251093
#Kelas = TPL B1 
#=================================================

#=================================================
# Materi Rekursif : Faktorial
# Recursive case => 3! = 3x2x1 
# base case => 0 berhenti
#=================================================

def faktorial(n):
    if n==0:
        return 1

    #recursive case
    return n*faktorial(n-1)


print("=========== Penghitung Faktorial =================")
print("Hasil Faktorial : ", faktorial(int(input("Masukkan angka anda : "))))
