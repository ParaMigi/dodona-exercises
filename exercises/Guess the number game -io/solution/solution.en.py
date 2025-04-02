antwoord = int(input("Player 1, give a number: "))
gok = ""
while gok != antwoord:
    gok = int(input("Player 2, guess the number: "))
    if gok > antwoord:
        print(f"The correct number is lower than {gok}")
    elif gok < antwoord:
        print(f"The correct number is higher than {gok}")
    else:
        print(f"Congratulations! {gok} is the correct number!")