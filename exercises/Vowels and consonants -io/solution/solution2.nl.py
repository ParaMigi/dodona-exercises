woordOfZin = input("Geef een woord of zin: ")
klinkers = "aeiou"
medeklinkers = "bcdfghjklmnpqrstvwxz"
aantalKlinkers = 0
aantalMedeklinkers = 0
for char in woordOfZin:
    if char in klinkers:
        aantalKlinkers += 1
    elif char in medeklinkers:
        aantalMedeklinkers += 1
print("Klinkers:", aantalKlinkers)
print("Medeklinkers:", aantalMedeklinkers)