# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
'שאלה:\n1. השלם את התנאים למיון עולה.\n2. שנה אותו ליורד'

'תשובה:\n1. שנה את תנאי ה-while ל-data[j] > מקש לעלייה.\n2. שנה את תנאי ה-while ל-data[j] < מקש לירידה.'
#1. עולה
# def insertion_sort(data):
#     for i in range(1, len(data)):
#         מפתח = נתונים[i]
#         j = i - 1
#         while j >= 0 and data[j] > key: #Ascending
#             נתונים[j + 1] = נתונים[j]
#             j -= 1
#     data[j + 1] = מפתח
#     return data

# #2. יורד
# def insertion_sort_descending(data):
#     for i in range(1, len(data)):
#         מפתח = נתונים[i]
#         j = i - 1
#         while j >= 0 and data[j] < key: #Descending
#             נתונים[j + 1] = נתונים[j]
#             j -= 1
#     data[j + 1] = מפתח
#     return data