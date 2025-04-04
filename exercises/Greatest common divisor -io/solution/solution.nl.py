a = int(input("Geef het eerste getal: "))
b = int(input("Geef het tweede getal: "))
kleinste = min(a, b)
ggd = 1
for n in range(2, kleinste+1):
    if (a % n == 0) and (b % n == 0):
        ggd = n
print(f"De grootste gemene deler van {a} en {b} is {ggd}.")