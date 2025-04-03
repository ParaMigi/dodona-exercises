getal = kleinste = grootste = int(input("Geef een getal"))
while getal != 0:
    if getal < kleinste:
        kleinste = getal
    if getal > grootste:
        grootste = getal
    getal = int(input("Geef nog een getal"))
print(f"Het kleinste van de getallen is {kleinste}, en het grootste is {grootste}.")