son1 = float(input("1-son: "))
son2 = float(input("2-son: "))
amal = input("Amal (+, -, *, /): ")

if amal == '+':
    print(f"Natija: {son1} + {son2} = {son1 + son2}")
elif amal == '-':
    print(f"Natija: {son1} - {son2} = {son1 - son2}")
elif amal == '*':
    print(f"Natija: {son1} * {son2} = {son1 * son2}")
elif amal == '/':
    if son2 == 0:
        print("Nolga bo'lish mumkin emas!")
    else:
        print(f"Natija: {son1} / {son2} = {son1 / son2}")
else:
    print("Noto'g'ri amal. Faqat +, -, *, / ishlatiladi.")