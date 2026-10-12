# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093

# ==========================================================
# משימות מעשית: מערכת תורים לסדנאות אופנועים
# ==========================================================

# מחלקת צומת: מאחסן נתונים של לקוח אחד בתור
class Node:
    def __init__(self, no, nama, servis):
        # לא: מספר תור
        # שם: שם הלקוח
        # שירות: סוג השירות הרצוי
        # הבא: מצביע לצומת הבא
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None

# שיעור תור סדנאות: מיישמת תור (FIFO - First In First Out) לסדנאות
class QueueBengkel:
    def __init__(self):
        # חזית: מצביע ללקוח הקדמי ביותר (מי יוגש ראשון)
        # אחורי: מצביע ללקוח האחורי ביותר (הלקוח האחרון שנכנס)
        self.front = None
        self.rear = None

    def is_empty(self):
        # בדוק אם התור ריק
        # אם החזית היא None זה אומר שאין לקוחות בתור
        return self.front is None

    def enqueue(self, no, nama, servis):
        # הוספת לקוחות חדשים לחלק האחורי של התור
        # צור צומת חדש עם נתוני לקוחות
        nodeBaru = Node(no, nama, servis)

        # אם התור ריק, הצמתים החדשים הופכים קדמיים ואחוריים
        if self.is_empty():
            self.front = nodeBaru
            self.rear  = nodeBaru
            print(f"Pelanggan {nama} ditambahkan ke antrian")
            return

        # אם התור לא ריק, הוסף צומת חדש מאחור
        # חבר את הצומת האחורי הישן עם הצומת החדש
        self.rear.next = nodeBaru
        # עדכן את האחורי לצומת חדש
        self.rear = nodeBaru
        print(f"Pelanggan {nama} ditambahkan ke antrian")


    def dequeue(self):
        # שירות לקוחות קו ראשון (ראשון בתור)
        # בדוק אם יש לקוחות בתור
        if self.is_empty():
            print('תור ריק, לא מתקנים אופנועים!')
            return None

        # שמור את נתוני הלקוח שיוצגו במשתנה
        nodeDilayani = self.front

        # הזז את המצביע הקדמי לצומת הבא
        self.front = self.front.next

        # אם החזית הופכת ללא (כלומר כל הלקוחות טופלו)
        # אז גם האחורי חייב להיות ללא כך שהתור ריק לחלוטין
        if self.front is None:
            self.rear = None

        # הצג נתוני לקוחות שזה עתה הוגשו
        print(f"Pelanggan {nodeDilayani.nama} sedang dilayani (Servis: {nodeDilayani.servis})")

        return nodeDilayani

    def tampilkan(self):
        # מציג את כל התור מלפנים (הכי מלפנים) לאחור (הרוב מאחור)
        print('רשימת תורים לסדנאות אופנועים (קדמי -> אחורי):')

        # החל מהצומת הקדמי (קדמי)
        current = self.front
        no = 1

        # עברו בלולאה בין כל הצמתים בתור
        while current is not None:
            # הצגת נתונים עבור כל לקוח בתור
            print(f"{no}. No Antrian: {current.no}, Nama: {current.nama}, Servis: {current.servis}")
            # עבור לצומת הבא
            current = current.next
            no += 1


def main():
    # צור מופע של תור לסדנאות
    q = QueueBengkel()

    # לולאת תפריט ראשי
    while True:
        print('=== מערכת תורים לסדנאות ===')
        print('1. הוסף לקוחות')
        print('2. לשרת את הלקוחות')
        print('3. תור הצג')
        print('4. צא')

        pilih = input('בחר תפריט:')

        # תפריט 1: הוסף לקוח חדש לתור
        if pilih == "1":
            no = input('מספר תור:')
            nama = input('שם:')
            servis = input('שירות:')
            q.enqueue(no, nama, servis)

        # תפריט 2: משרתים את הלקוח בקדמת התור
        elif pilih == "2":
            q.dequeue()

        # תפריט 3: הצג את כל הלקוחות בתור
        elif pilih == "3":
            print("\n")
            q.tampilkan()

        # תפריט 4: צא מהתוכנית
        elif pilih == "4":
            print('תודה על השימוש במערכת התורים לסדנאות!')
            break

        # אם הבחירה אינה תואמת לתפריט הקיים
        else:
            print('בחירה לא חוקית')

# הפעל את התוכנית הראשית כאשר קובץ זה מבוצע ישירות
if __name__ == "__main__":
    main()
