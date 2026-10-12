#=================================================
# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093
# תרגיל 3: חיפוש BST
#=================================================


class Node:
    def __init__(self, data):  #אתחול
        self.data = data
        self.right = None
        self.left = None

def insert(root,data): #הוספת צמתים
    if root is None: #אם אין עדיין צמתים, צור צומת חדש
        return Node(data)

    if data<root.data:  # אם הנתונים קטנים יותר, החלק שמאלה
        root.left = insert(root.left,data)
    elif data>root.data: #אם הוא גדול יותר, החלק ימינה
        root.right = insert(root.right,data)

    return root

#מלא את נתוני BST
root = None
data_list = [50,30,70,20,40,50,80]
for data in data_list:
    root = insert(root,data)

def search(root,key): #חפש נתונים ב-BST
    if root is None: #אם הצומת ריק
        return False

    if root.data == key: #אם נמצא נתונים
        return True

    if key < root.data: #אם המפתח קטן יותר, הסתכל בצד שמאל
        return search(root.left,key)
    else: #אם המפתח גדול יותר, הסתכל בצד ימין
        return search(root.right,key)

#חיפוש בדיקה
key = 40
if search(root,key) is True:
    print('נמצאו נתונים')
else:
    print('הנתונים לא נמצאו')