gok = input("Geef het wachtwoord in: ")
pogingen = 1
while gok != "InformaticaWetenschappen!":
    print("Fout wachtwoord - poging", pogingen, "- probeer opnieuw")
    gok = input("Geef het wachtwoord in: ")
    pogingen += 1
print("Correct wachtwoord")