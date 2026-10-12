# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # הוספת צומת מקדימה (ראש)
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # מוחק צמתים על סמך מפתח
    def delete_node(self, key):
        temp = self.head

        # 1. אם צומת הראש מחזיק את המפתח שמחפשים
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            print(f"Berhasil menghapus {key}.")
            return

        # 2. חפש את המפתח בשאר הרשימה
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # 3. אם המפתח לא נמצא
        if temp is None:
            print(f"Nilai {key} tidak ditemukan dalam list.")
            return

        # 4. בטל קישור של צמתים
        prev.next = temp.next
        temp = None
        print(f"Berhasil menghapus {key}.")

    # הדפס את תוכן הרשימה
    def print_list(self):
        temp = self.head
        if temp is None:
            print('(רשימה ריקה)')
            return
        print('תוכן הרשימה הנוכחית:', end="")
        while temp:
            print(f" {temp.data} ->", end="")
            temp = temp.next
        print(" ריק")

# --- חלקים עיקריים ---
if __name__ == "__main__":
    llist = LinkedList()

    # --- הנתונים מסופקים כאן ---
    # אתה יכול לשנות את המספרים בסוגריים מרובעים אלה
    angka_bawaan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # הזנת נתונים לרשימה המקושרת
    # אנו הופכים את זה כך שהסדר על המסך זהה לסדר ברשימת default_number
    for angka in reversed(angka_bawaan):
        llist.push(angka)

    print('=== תוכנית למחיקת צמתים (נתונים מוגדרים מראש) ===')

    # קפוץ ישר ללולאה האינטראקטיבית
    while True:
        print("\n--------------------------------")
        # 1. הצג את המצב הנוכחי של הרשימה
        llist.print_list()

        # 2. בדוק אם הרשימה הסתיימה
        if llist.head is None:
            print('הרשימה ריקה. אי אפשר למחוק שום דבר.')
            print('התוכנית נעצרת.')
            break

        # 3. אישור משתמש
        tanya = input("\nהאם ברצונך למחוק את הצומת? (y/n): ").lower()
        if tanya != 'y':
            print('התוכנית הושלמה. תודה לך!')
            break

        # 4. תהליך קלט ומחיקה
        try:
            key_hapus = int(input('הזן את המספרים שברצונך למחוק:'))
            llist.delete_node(key_hapus)
        except ValueError:
            print('❌ שגיאה: נא להזין רק מספרים עגולים.')