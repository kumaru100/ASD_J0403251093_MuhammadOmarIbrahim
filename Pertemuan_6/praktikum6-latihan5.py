# Nama : Muhammad Omar Ibrahim
# NIM : J0403251093

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
    else:
        result.append(right[j])
        j += 1
        result.extend(left[i:])
        result.extend(right[j:])
    return result
'''
Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().
'''

'''
Jawaban:
1. Ubah kondisi if menjadi left[i] < right[j] untuk ascending.
2. result.extend() digunakan untuk menambahkan semua elemen dari list yang diberikan ke dalam list
'''

#1. Ascending
# def merge(left, right):
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result