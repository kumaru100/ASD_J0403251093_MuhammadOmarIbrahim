#===============================================================
# שם: מוחמד עומר איברהים
# מספר סטודנט : J0403251093
#===============================================================
#===============================================================
#מיזוג מיון (עולה)
#================================================================

def merge_sort(data, depth=0):
    indent = "  " * depth#הזחה המבוססת על נתונים רקורסיביים
    print(f"{indent}merge_sort({data})")#מציג את הנתונים שנמצאים כעת בעיבוד

    if len(data)<=1:
        return data

    #מחלקים: מחלקים את הנתונים ל-2 חלקים
    mid=len(data)//2
    left=data[:mid]#חיתוך שמאל
    right=data[mid:]#חיתוך נכון

    print(f"{indent}divide -> left = {left} | right = {right}")#מציג את תוצאות החלוקה
        #שיחות רקורסיביות
    left_sorted=merge_sort(left)
    right_sorted=merge_sort(right)

    merged = merge(left_sorted,right_sorted)
    print(f"{indent}merge -> {left_sorted}-{right_sorted}={merged}")#מציג את תוצאות המיזוג

    return merge(left_sorted,right_sorted)

def merge(left,right):
    result=[]
    i=0
    j=0

    #משווה בין אלמנטים משמאל לימין
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    #הוסף את הרכיבים הנותרים אם יש
    result.extend(left[i:])
    result.extend(right[j:])

    return result


angka=[13,7,28,5,19,36,4]
print('נתונים לפני מיון:', angka)
print('נתונים לאחר מיון:', merge_sort(angka))


'1. תשובה ראשונה\n2. תשובה שניה\n3. תשובה שלישית   \n4. תשובה רביעית\n5. תשובה חמישית\n6. תשובה שישית\n7. תשובה שביעית\n8. תשובה שמינית\n9. תשובה תשיעית\n10. תשובה עשירית'