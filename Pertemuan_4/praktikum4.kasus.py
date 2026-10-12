#=============================================
# שם : Muhammad Omar Ibrahim
#מספר סטודנט : J0403251093
#=============================================

#=============================================
#מקרה מבחן: מערכת תורים של שירות אקדמי
#יישום תור =>
# תור: הזז את המצביע לאחור (הוסף נתונים חדשים)
# תור: הזז את המצביע הקדמי (מחק נתונים מלפנים)
# מחסנית ==> חזית -> C -> B -> A -> אין
# קדמי -> A -> C -> אחורי
#=============================================

#1) הגדרת צמתים (יחידה בסיסית של רשימה מקושרת)
class Node:
    def __init__(self, nim, nama):
        self.nim   = nim   #שמור תלמיד NIM
        self.nama  = nama  #שמור שמות תלמידים
        self.next  = None  #מצביע לצומת הבא (התחלה)
#2) הגדרת התור
class queueAkademik:
    def __init__(self):
        self.front = None #הצומת הקדמי
        self.rear  = None #הצומת האחורי ביותר


    def is_empty(self):
        #כאשר התור ריק אז קדמי = אחורי = אין
        return self.front is None

    #הוספת נתונים חדשים לחלק האחורי (האחורי) => הוספת תור של סטודנטים הפונים לשירותים אקדמיים
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama)
        #אם נתונים חדשים נכנסים מתוך תור ריק אז נתונים חדשים = קדמי = אחורי
        if self.is_empty():
            self.front = nodeBaru
            self.rear  = nodeBaru
            return
        #אם התור לא ריק, נתונים חדשים ממוקמים אחרי אחורי ואז הופכים לאחור

        self.rear.next = nodeBaru
        self.rear = nodeBaru

    #מחיקת נתונים חזיתיים (מתן שירותים אקדמיים)
    def dequeue(self):

        if self.is_empty():
            print('תור ריק, ללא סטודנטים!!!')
            return None

        #הצג את נתוני החזית, שמור אותם במשתנה למחיקה
        nodeDilayani = self.front

        #הזז את המצביע הקדמי לצומת הבא
        self.front = self.front.next

        #אם החזית הופכת ללא (נתוני התור האחרון שהוגשו), אז קדמי = אחורי = אין
        if self.front is None:
            self.rear = None

        return nodeDilayani

    def tampilkan(self):



        print('רשימת תורים לסטודנטים (קדמי -> אחורי):')
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}.{current.nim} = {current.nama}")
            current = current.next
            no += 1

#תוכנית ראשית

def main():

    #מופע תור
    q = queueAkademik()

    while True:
        print('========== מערכת תורים אקדמית ==========')
        print('1. הוסף תלמידים')
        print('2. לשרת את התלמידים')
        print('3. תור הצג')
        print('4. צא')

        pilihan = input('בחר תפריט (1-4):').strip()

        if pilihan == "1":
            nim = input('הזן NIM:').strip()
            nama = input('הזן שם:').strip()

            q.enqueue(nim,nama)
            print('סטודנט נוסף בהצלחה')
        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print('התוכנית הושלמה, תודה')
            break

        else:
            print('בחירה לא חוקית, נסה שוב 1-4')

#סמן ביצוע קובץ ראשי
if __name__ == "__main__":
    main()
