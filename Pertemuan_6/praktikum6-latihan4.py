# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093

def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


'שאלה:\n1. מה הכוונה בבסיס מקרה?\n2. למה הפונקציה קוראת לעצמה?\n3. מה המטרה של הפונקציה merge()?'

'תשובה:\n1. מקרה בסיס הוא המצב שבו הפונקציה מפסיקה לחזור על עצמה, כלומר כאשר לנתונים יש אלמנט 0 או 1.\n2. הפונקציה קוראת לעצמה לחלק את הנתונים לחלקים קטנים יותר עד שהם מגיעים למקרה הבסיסי.\n3. הפונקציה merge() שואפת לשלב שני חלקים של נתונים ממוינים לחלק ממוין אחד.'