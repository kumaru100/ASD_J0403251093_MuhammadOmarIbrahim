#===============================================================
# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093
#================================================================

#================================================================
#Insertion Sort(Ascending)
#================================================================

def insertion_sort(data):
    #Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1,len(data)):
        key = data[i]#Simpan nilai yang disisipkan
        j = i-1 #index elemen terakhir di bagian kiri
        
        #Geser
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key
    return data


angka=[7,8,5,2,4,6]
print("Data sebelum diurutkan:", angka)
print("Data setelah diurutkan:", insertion_sort(angka))