
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
'''
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending.
2. Ubah agar menjadi descending
'''

'''
Jawaban:
1. Ubah kondisi while menjadi data[j] > key untuk ascending.
2. Ubah kondisi while menjadi data[j] < key untuk descending.
'''
#1. Ascending
# def insertion_sort(data):
#     for i in range(1, len(data)):
#         key = data[i]
#         j = i - 1
#         while j >= 0 and data[j] > key: #Ascending
#             data[j + 1] = data[j]
#             j -= 1
#     data[j + 1] = key
#     return data

# #2. Descending
# def insertion_sort_descending(data):
#     for i in range(1, len(data)):
#         key = data[i]
#         j = i - 1
#         while j >= 0 and data[j] < key: #Descending
#             data[j + 1] = data[j]
#             j -= 1
#     data[j + 1] = key
#     return data