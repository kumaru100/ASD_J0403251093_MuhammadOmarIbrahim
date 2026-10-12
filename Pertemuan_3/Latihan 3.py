# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # פונקציה להוספת אלמנטים בסוף (כדי להתאים את סדר הקלט)
    def append(self, new_data):
        new_node = Node(new_data)

        # אם הרשימה ריקה, הצומת החדש הופך לראש
        if self.head is None:
            self.head = new_node
            return

        # אחרת, יש להתעמק עד הצומת האחרון
        last = self.head
        while last.next:
            last = last.next

        # חבר את הצומת האחרון לצומת החדש
        last.next = new_node
        new_node.prev = last

    # --- פונקציית חיפוש (תרגיל 3) ---
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True # נמצא אלמנט
            current = current.next
        return False # האלמנט לא נמצא לאחר השלמת הלולאה

    # פונקציית עזר להצגת רשימה
    def print_list(self):
        node = self.head
        print('תוכן רשימה:', end="")
        while node:
            print(f"{node.data}", end=" <-> " if node.next else "")
            node = node.next
        print()

# --- מקטע אינטראקטיבי כדוגמה ---
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # 1. רכיבי קלט (הדמיית קלט משתמש: 2, 6, 9, 14, 20)
    raw_input = input('הוסף אלמנטים לרשימה כפולה מקושרת (הפרד אותם בפסיקים):')
    # ממירה את מחרוזת הקלט "2, 6, 9..." לרשימה של מספרים שלמים
    elements = [int(x.strip()) for x in raw_input.split(',')]

    for el in elements:
        dll.append(el)

    # 2. הזן את האלמנט שאתה מחפש
    cari = int(input('הזן את האלמנט שברצונך לחפש:'))

    # 3. ביצוע חיפוש
    ditemukan = dll.search(cari)

    # 4. הצג תוצאות
    if ditemukan:
        print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
    else:
        print(f"Elemen {cari} TIDAK ditemukan dalam Doubly Linked List.")
        #מבחן