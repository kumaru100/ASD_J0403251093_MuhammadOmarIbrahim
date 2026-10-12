#=================================================
# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093
# תרגיל 2: מעבר בסדר inorder
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


def inorder(root): # מעבר בסדר inorder
    if root is not None: #אם הצומת לא ריק
        inorder(root.left) #בקר בעץ המשנה השמאלי
        print(root.data, end=' ') #הצג נתוני צומת
        inorder(root.right) #בקר בעץ המשנה הימני

print('תוצאות לפי סדר:') #מציג תוצאות מעבר
inorder(root) #מבצע מעבר סדר

