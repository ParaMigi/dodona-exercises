aantal_woorden = int(input("Hoeveel woorden wil je zeggen? "))
som = 0
for i in range(aantal_woorden):
    woord = input(f"Geef het {i+1}e woord: ")
    som += len(woord)
print(f"De som van het aantal letters in de woorden is {som}.")