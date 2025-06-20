
yosh = int(input("Yoshingizni kiriting: "))
narx = 100

if yosh <= 6:
    narx = narx * 0.5

if yosh >= 7 and yosh <= 17:
    narx = narx * 0.8

if yosh > 60:
    narx = narx * 0.7

print("Yakuniy narx:", narx, "so'm")