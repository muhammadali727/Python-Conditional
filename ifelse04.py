balans = 5000
summa = int(input("Yechmoqchi bo'lgan summani kiriting: "))

if summa <= balans:
    balans = balans - summa
    print(f"Pul yechildi. Qolgan balans: {balans} so'm")

if summa > balans:
    print(f"Mablag' yetarli emas. Sizning balansingiz: {balans} so'm")
