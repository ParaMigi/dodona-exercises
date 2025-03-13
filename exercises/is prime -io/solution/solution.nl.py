getal = int(input("Geef een getal: "))

isPriem = True

for i in range(2, getal): # range(2, round(1 + getal**(1/2))) is sneller
    if getal % i == 0:
        isPriem = False

if isPriem:
    print(getal, "is priem")
else:
    print(getal, "is niet priem")