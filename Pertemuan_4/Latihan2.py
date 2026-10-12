#================================================
# יישום בסיסי: צמתים ברשימה מקושרת
# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093
#================================================

# צור מחלקת Node (היא היחידה הבסיסית של רשימה מקושרת)
class Node:
    def __init__(self, data): #בנאי לאתחול צומת
        self.data = data #לאחסן ערכי נתונים
        self.next = None #מצביע לצומת הבא
#1) צור צמתים אחד אחד
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) צמתים מחברים: A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

#3) קבע את הצומת הראשון (ראש)
head = nodeA

#4) חציה: התחקות מראש לאף אחד
current = head
while current is not None:
    print(current.data) #מציג נתונים על הצומת הנוכחי
    current = current.next #עבור לצומת הבא

#================================================
# יישום בסיסי: רשימה מקושרת + הוספה ראשונית
#================================================

class LinkedList: #class implementasi stack
    def __init__(self):
        self.head = None #בהתחלה הוא היה ריק


    def insert_awal(self, data): #דחוף קונספט בערימה
        #1) צור צומת חדש
        nodeBaru=Node(data) #התקשר למחלקת הצומת
        #2) הצומת החדש מצביע על הראש הישן
        nodeBaru.next = self.head
        #3) ראש עובר לצומת חדש
        self.head = nodeBaru

    def hapus_awal(self): #קונספט פופ בערימה
        data_terhapus = self.head.data #להציץ בערימה
        self.head = self.head.next  #מעביר את הראש לצומת הבא
        print('נתונים שנמחקו:', data_terhapus)

    def tampilkan(self): #יישום חציה
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print('======= רשימה חדשה =======')
ll = LinkedList() #הצג את האובייקט במחלקת הרשימה המקושרת
ll.insert_awal("X") #הכנס צומת עם הנתונים "X"
ll.insert_awal("Y") #הכנס צומת עם הנתונים "Y"
ll.insert_awal("Z") #הכנס צומת עם הנתונים "Z"
ll.tampilkan() #מציג את תוכן הרשימה המקושרת
ll.hapus_awal() #מחק את הצומת הראשון (Z)
ll.tampilkan() #מציג את התוכן של רשימה מקושרת לאחר המחיקה
