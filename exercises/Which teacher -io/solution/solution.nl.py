klas = input("In welke klas zit je? ")
if klas == "4NW4":
    print("Jouw leerkracht voor informaticawetenschappen is Mevr. Derck.")
elif klas == "4NW3":
    print("Jouw leerkracht voor informaticawetenschappen is Mevr. Michiels.")
elif klas in ("4NW2", "4NW1", "4EW2", "4EW1"):
    print("Jouw leerkracht voor informaticawetenschappen is Mr. Atsma.")
else:
    print("Jij krijgt geen informaticawetenschappen.")