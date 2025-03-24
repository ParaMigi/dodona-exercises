klas = input("Which class are you in? ")
if klas == "4NW4":
    print("Your teacher for computer science is Ms. Derck.")
elif klas == "4NW3":
    print("Your teacher for computer science is Mrs. Michiels.")
elif klas in ("4NW2", "4NW1", "4EW2", "4EW1"):
    print("Your teacher for computer science is Mr. Atsma.")
else:
    print("You don't take computer science.")