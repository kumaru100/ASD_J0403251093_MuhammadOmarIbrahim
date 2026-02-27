# ==========================================================
# Studi Kasus: Generator PIN 3 Digit (0–2)
# ==========================================================

def buat_pin(panjang, hasil=""):
    
    # Base case
    # Jika panjang string 'hasil' sudah sama dengan panjang PIN,
    # maka PIN sudah lengkap dan siap dicetak
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Recursive case
    # Coba setiap kemungkinan angka (choose)
    for angka in ["0", "1", "2"]:
        
        # Explore → tambahkan angka ke hasil saat ini
        buat_pin(panjang, hasil + angka)


# Membuat PIN 3 digit
buat_pin(3)