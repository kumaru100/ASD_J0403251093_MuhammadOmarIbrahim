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
    #Base case berhenti ketika n == 0
    if n==0:
        return 1

    #recursive case masalah diperkecil jadi  faktorial n-1
    return n*faktorial(n-1)


print("=========== Penghitung Faktorial =================")
print("Hasil Faktorial : ", faktorial(int(input("Masukkan angka anda : "))))
