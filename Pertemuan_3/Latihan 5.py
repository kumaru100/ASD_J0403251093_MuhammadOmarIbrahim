# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # פונקציה להוספת אלמנטים בסוף (הוספה)
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # --- פונקציה הפוכה (תרגיל 5) ---
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next  # 1. שמור את הצומת הבא כדי שלא ילך לאיבוד
            current.next = prev       # 2. הפוך את המצביע לצומת הקודם
            prev = current            # 3. החלק את 'קודם' קדימה ל'נוכחי'
            current = next_node       # 4. העבר את 'נוכחי' קדימה ל-'next_node'

        self.head = prev  # עדכן ראש לצומת האחרון (שהוא עכשיו ראשון)

    # פונקציה להדפסת רשימה לפי הפורמט לדוגמה
    def print_list(self):
        temp = self.head
        if temp is None:
            print("null")
            return
        while temp:
            print(f"{temp.data}", end=" -> ")
            temp = temp.next
        print("null")

# --- הפעלת התוכנית על פי הדוגמה ---
if __name__ == "__main__":
    llist = LinkedList()

    # קלט משתמש
    try:
        raw_input = input('הזן את הרכיבים עבור הרשימה המקושרת (הפרד אותם בפסיקים):')
        if raw_input.strip(): # בדוק אם הקלט אינו ריק
            elements = [int(x.strip()) for x in raw_input.split(',')]
            for el in elements:
                llist.append(el)

        # לפני צפייה
        print('רשימה מקושרת לפני היפוך:', end="")
        llist.print_list()

        # תהליך היפוך
        llist.reverse()

        # לאחר הצגה
        print('רשימה מקושרת לאחר הפוך:', end="")
        llist.print_list()

    except ValueError:
        print('שגיאת קלט: הקפד להזין מספרים מופרדים בפסיקים.')

        #מבחן