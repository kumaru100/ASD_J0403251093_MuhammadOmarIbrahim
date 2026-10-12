#================================================
# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093
#================================================

#================================================
# יישום בסיסי: תור מבוסס על רשימה מקושרת
#================================================

class Node:
    def __init__(self, data): #בנאי לאתחול צומת
        self.data = data #לאחסן ערכי נתונים
        self.next = None #מצביע לצומת הבא

#תור עם 2 מצביעים: מלפנים ומאחור
class QueueLL:
    def __init__(self):
        self.front = None #הצומת הקדמי
        self.rear = None #הצומת האחורי ביותר

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        #הוספת נתונים מאחור (זנב)
        nodeBaru = Node(data)

        #אם התור ריק, מלפנים ומאחור מצביעים על אותו צומת
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #האחורי עובר לצומת חדש
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    def dequeue(self):
        #מחק נתונים מהחזית (הראש)

        #1) הציצו/הסתכלו על הנתונים הקדמיים
        data_terhapus = self.front.data

        #2) העבר את החזית לצומת הבא
        self.front = self.front.next

        #3) אם לאחר החלקה קדמית הוא הופך ללא, זה אומר שהתור ריק
        #ואז האחורי הוא גם ללא
        if self.front is None:
            self.rear = None


    def tampilkan(self):
        #מציג את תוכן התור מלפנים לאחור
        current = self.front
        print('חזית', end=" -> ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print('אין - אחורי בצומת האחרון')

#מופע של אובייקטים בתור כיתה
q=QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()