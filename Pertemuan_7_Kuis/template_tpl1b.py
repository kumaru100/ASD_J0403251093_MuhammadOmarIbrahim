# ==============================================================================
# תרגול מבחן אמצעי - אלגוריתם ומבנה נתונים (TPL2106)
# שם    : Muhammad Omar Ibrahim
# מספר סטודנט     : J0403251093
# כיתה   : TPL B1
# ==============================================================================


# ==============================================================================
# 1. טיפול בקבצים ומילון
# פונקציה זו משמשת לקריאת קובץ Buku.txt ולאחר מכן לשמור אותו
# לתוך מבנה הנתונים של מילון לגישה נוחה על סמך קוד הספר
# ==============================================================================
def muat_data_buku(nama_file):
    "פונקציה לקריאת 'book.txt' ולשמור אותו במילון.\n    פורמט קובץ: book_code, כותרת, מחיר"

    # מילון לאחסון כל נתוני הספר
    database_buku = {}

    try:
        # פתיחת קבצים במצב קריאה (r).
        with open(nama_file, 'r') as file:

            # קורא כל שורה בקובץ
            for line in file:

                # הסר את השורה החדשה ואז הפרד את הנתונים על סמך פסיקים
                kode, judul, harga = line.strip().split(',')

                # שמור נתונים למילון
                # מפתח = קוד ספר
                # ערך = מילון המכיל כותרות ומחירים
                database_buku[kode] = {
                    'Judul': judul,
                    'Harga': int(harga)
                }

                # מציג נתונים שנקראו בהצלחה
                print(f"Kode: {kode}, Judul: {judul}, Harga: {harga}")

    # אם הקובץ לא נמצא
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

    # תפוס שגיאות אחרות שעלולות להתרחש
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")

    # מחזירה מילון המכיל נתוני ספר
    return database_buku



# ==============================================================================
# 2. רשימה מקושרת - ניהול קידום מכירות
# משמש לאחסון רשימה של ספרים שמקודמים
# משתמש במבנה של רשימה מקושרת
# ==============================================================================

# מחלקת הצומת היא האלמנט הבסיסי של הרשימה המקושרת
class Node:
    def __init__(self, judul):
        self.judul = judul   # נתונים מאוחסנים (שם הספר)
        self.next = None     # מצביע לצומת הבא


class LinkedListPromosi:

    # בונה רשימות מקושרות
    def __init__(self):
        self.head = None   # הצומת הראשון ברשימה המקושרת

    # הוסף ספר לרשימת המבצעים
    def tambah_buku_promosi(self, judul):

        # צור צומת חדש
        baru = Node(judul)

        # אם הרשימה המקושרת עדיין ריקה
        if self.head is None:
            self.head = baru
        else:
            # אם כבר יש תוכן, חפש את הצומת האחרון
            current = self.head
            while current.next:
                current = current.next

            # הצומת החדש מתווסף בסוף הרשימה
            current.next = baru

    # מציג את כל הרשימה של ספרי קידום מכירות
    def tampilkan_promosi(self):
        print('רשימת ספרי קידום מכירות:')

        current = self.head
        nomor = 1

        # מעבר מראש לקצה
        while current:
            print(f"{nomor}. {current.judul}")
            current = current.next
            nomor += 1



# ==============================================================================
# 3. תור - תור קופה
# מבנה הנתונים בתור משמש לניהול תורי לקוחות
# עם קונספט ה-FIFO (First In First Out).
# ==============================================================================

class AntreanKasir:

    def __init__(self):
        # הצומת בקדמת התור
        self.front = None

        # הצומת בחלק האחורי של התור
        self.rear = None

    # בודק אם התור ריק
    def is_empty(self):
        return self.front is None

    # ENQUEUE -> מוסיף לקוח לתור
    def tambah_antrean(self, nama_pelanggan):

        # צור צומת חדש עבור הלקוח
        antreanBaru = Node(nama_pelanggan)

        # אם התור ריק
        if self.is_empty():
            self.front = antreanBaru
            self.rear = antreanBaru
        else:
            # הוסף לחלק האחורי של התור
            self.rear.next = antreanBaru
            self.rear = antreanBaru

        print(f"{nama_pelanggan} masuk ke antrean.")

    # DEQUEUE -> שירות לקוחות בחזית
    def layani_pelanggan(self):

        # אם התור ריק
        if self.is_empty():
            print('קו ריק, אין לקוחות.')
            return

        # קח את הלקוח בחזית
        pelanggan_dilayani = self.front.judul

        # העבר את החזית לצומת הבא
        self.front = self.front.next

        # אם לאחר ההגשה התור הופך לריק
        if self.front is None:
            self.rear = None

        print(f"Pelanggan {pelanggan_dilayani} telah dilayani.")

    # מציג את כל תור הלקוחות
    def tampilkan_antrean(self):

        if self.is_empty():
            print('השורה ריקה.')
            return

        current = self.front
        nomor = 1

        print('רשימת תור:')

        # מעבר תור מלפנים לאחור
        while current:
            print(f"{nomor}. {current.judul}")
            current = current.next
            nomor += 1



# ==============================================================================
# 4. מיון - דוחות עסקה
# מיין נתוני עסקאות באמצעות אלגוריתם מיון הוספה
# ==============================================================================

def urutkan_transaksi(list_harga):
    'מיין את המחירון באמצעות מיון הכנסה'

    # צור עותק של הרשימה כדי שהנתונים המקוריים לא ישתנו
    hasil = list_harga.copy()

    # הלולאה מתחילה מהאלמנט השני
    for i in range(1, len(hasil)):

        key = hasil[i]   # ערך שיוכנס
        j = i - 1

        # מעביר אלמנטים גדולים מהמפתח ימינה
        while j >= 0 and hasil[j] > key:
            hasil[j + 1] = hasil[j]
            j -= 1

        # הנח את המפתח במיקום הנכון
        hasil[j + 1] = key

    # מחזיר רשימה ממוינת
    return hasil



# ==============================================================================
# תוכנית ראשית - תפריט ממשק
# התוכנית הראשית שמפעילה את כל תכונות המערכת
# ==============================================================================

def main():

    # אתחול הנתונים הראשוניים

    file_db = "buku.txt"

    # קרא נתוני ספר מהקובץ
    data_buku = muat_data_buku(file_db)

    # צור אובייקט פרסומי של רשימה מקושרת
    list_promosi = LinkedListPromosi()

    # צור אובייקט בתור קופאי
    antrean_toko = AntreanKasir()

    # דוגמה לנתוני עסקה
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]



    # לולאת תפריט ראשי
    while True:

        print('--- מערכת ניהול חנות ספרים ---')
        print("1. הצג את קטלוג הספרים (מילון/קובץ)")
        print('2. נהל רשימת קידום מכירות (רשימה מקושרת)')
        print('3. ניהול תור קופאי (תור)')
        print('4. הצג דוחות מכירות ממוינים (מיון)')
        print('5. צאו החוצה')

        pilihan = input('בחר תפריט (1-5):')



        # MENU 1 -> מציג את קטלוג הספרים
        if pilihan == '1':
            print('קטלוג ספרים:', data_buku)



        # תפריט 2 -> הוסף ספר לרשימת המבצעים
        elif pilihan == '2':

            judul = input('הזן את כותרת הספר לקידום:').strip()

            list_promosi.tambah_buku_promosi(judul)
            list_promosi.tampilkan_promosi()



        # תפריט 3 -> נהל תורים בקופאיות
        elif pilihan == '3':

            print('1. הוסף תור')
            print('2. לשרת את הלקוחות')
            print('3. תור הצג')

            sub = input('בחר אפשרות:')

            # הוסף לקוחות לתור
            if sub == '1':
                nama = input('שם הלקוח:')
                antrean_toko.tambah_antrean(nama)

            # מתן שירות ללקוחות מובילים
            elif sub == '2':
                antrean_toko.layani_pelanggan()

            # מציג את התור
            elif sub == '3':
                antrean_toko.tampilkan_antrean()



        # MENU 4 -> מציג דוחות עסקאות ממוינים
        elif pilihan == '4':

            print('מחיר לפני מיון:', riwayat_transaksi)

            hasil_sort = urutkan_transaksi(riwayat_transaksi)

            print('מחיר לאחר עיסוי:', hasil_sort)



        # תפריט 5 -> צא מהתוכנית
        elif pilihan == '5':
            print('התוכנית הושלמה. תודה לך.')
            break



        # אם קלט התפריט אינו חוקי
        else:
            print('בחירה לא חוקית!')



# הפעל את התוכנית הראשית
if __name__ == "__main__":
    main()