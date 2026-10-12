#=================================================
# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093
# תרגיל 4: יצירת BST לא מאוזן
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


def preorder(root): #הזמנה מראש של מעבר
    if root is not None:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

def tampil_struktur(root, level=0, posisi='שורש'): #מציג את מבנה BST
    if root is not None:
        print(" "*level + f"{posisi}: {root.data}")
        tampil_struktur(root.left,level+1,"L")
        tampil_struktur(root.right,level+1,"R")


# -----------------------------
# תוכנית ראשית
# -----------------------------

print('הזמנות מוקדמות של BST:')
preorder(root)
print('מבנה BST:')
tampil_struktur(root)