# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093

#===============================================
#פרקטיקה 1: ADT ומושגי טיפול בקבצים
#תרגיל בסיסי 1: קרא את כל תוכן הקובץ
#===============================================


#פתח קובץ במצב read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()

print(isi_file)
print('===קריאת תוצאות===')
print('סוג נתונים:', type(isi_file))
print('מספר תווים', len(isi_file))
print('מספר שורות', isi_file.count("\n")+1)

print('===קריאה לכל שורה===')
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris +=1
        baris = baris.strip()
        print('שורה', jumlah_baris)
        print('תוכן:', baris)

#===============================================
#פרקטיקה 1: ADT ומושגי טיפול בקבצים
#תרגיל בסיסי 2: נתח שורות לעמודות של נתונים
#===============================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",")
        print('NIM:', nim, '|שם:', nama, '|ערך:', nilai)


#===============================================
#פרקטיקה 1: ADT ומושגי טיפול בקבצים
#תרגיל בסיסי 3: קריאת קבצים ושמירה ברשימה
#===============================================
#רשימה להכיל
data_list = []


with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",")
        #שמור כרשימה [שם, שם, ערך]
        data_list.append([nim,nama,int(nilai)])

print('=== נתוני תלמידים ברשימה ===')
print(data_list)

print('=== מספר הרשומות ברשימה ===')
print('מספר רשומות:', len(data_list))

print('=== מציג נתוני רשומות ספציפיות ===')
print('דוגמה לרשומה ראשונה:', data_list[0])

#===============================================
#פרקטיקה 1: ADT ומושגי טיפול בקבצים
#תרגיל בסיסי 4: קריאת קבצים ושמירה למילון
#===============================================

data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",")

        #לשמור את נתוני התלמידים למילון
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai),
        }
print('=== נתוני תלמידים במילון')
print(data_dict)

#===============================================
#בדוק התחייבות כדי שלא תראה את התיקיה מהעלאה
#===============================================