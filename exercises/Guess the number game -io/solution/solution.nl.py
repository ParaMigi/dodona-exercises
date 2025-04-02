antwoord = int(input("Speler 1, geef een getal: "))
gok = ""
while gok != antwoord:
    gok = int(input("Speler 2, doe een gok om het getal te raden: "))
    if gok > antwoord:
        print(f"Het juiste getal is lager dan {gok}")
    elif gok < antwoord:
        print(f"Het juiste getal is hoger dan {gok}")
    else:
        print(f"Gefeliciteerd! {gok} is het juiste getal!")