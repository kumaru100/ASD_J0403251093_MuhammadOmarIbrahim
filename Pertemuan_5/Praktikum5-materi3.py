#=================================================
#Nama = Muhammad Omar Ibrahim
#NIM = J0403251093
#Kelas = TPL B1 
#=================================================

#=================================================
# Materi Rekursif : Menjumlahkan Elemen List
#=================================================

def jumlah_list(data,index=0):
    #Base case : Jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    #Recursive case : Elemen sekarang + Jumlah elemen setelahnya
    return data[index] + jumlah_list(data,index+1)

print("==============Program Jumlah Data============")
print(jumlah_list([2,4,5,6,8]))