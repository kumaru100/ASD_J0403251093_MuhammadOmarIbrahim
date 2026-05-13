# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093

def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


'''
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?
'''

'''
Jawaban:
1. Base case adalah kondisi di mana fungsi berhenti melakukan rekursi, yaitu saat data memiliki 0 atau 1 elemen.
2. Fungsi memanggil dirinya sendiri untuk membagi data menjadi bagian yang lebih kecil hingga mencapai base case.
3. Fungsi merge() bertujuan untuk menggabungkan dua bagian data yang sudah terurut menjadi satu bagian yang terurut.'''