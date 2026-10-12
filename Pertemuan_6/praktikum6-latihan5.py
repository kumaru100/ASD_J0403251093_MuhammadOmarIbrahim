# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093

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
'שאלה:\n1. השלם את התנאים כדי להפוך לעולה.\n2. הסבר את הפונקציה result.extend() .'

'תשובה:\n1. שנה את התנאי אם לשמאל[i] < ימין[j] לעליה.\n2. result.extend() משמש להוספת כל הרכיבים של הרשימה הנתונה לרשימה'

#1. עולה
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