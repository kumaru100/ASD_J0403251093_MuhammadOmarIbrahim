# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093

def insertion_sort(data):
    # Loop dari elemen kedua sampai terakhir
    for i in range(1, len(data)):
        key = data[i]  # Elemen yang sedang ingin ditempatkan pada posisi yang benar
        j = i - 1      # Indeks elemen sebelumnya

        # Geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]  # Geser elemen ke kanan
            j -= 1                 # Pindah ke elemen sebelumnya

        # Tempatkan key pada posisi yang benar
        data[j + 1] = key

    # Kembalikan list yang sudah terurut
    return data
'''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?
'''

'''
Jawaban:
1. Elemen pertama (indeks 0) sudah dianggap tersort, mulai dari indeks 1.
2. Key menyimpan nilai elemen saat ini yang akan diurutkan.
3. While untuk geser elemen karena jumlah iterasi tidak pasti, for butuh jumlah tetap.
4. Menggeser elemen ke kanan (data[j+1] = data[j]) dan j -= 1 sampai posisi tepat.
'''