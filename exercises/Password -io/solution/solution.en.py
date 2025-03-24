guess = input("Give the password: ")
attempts = 1
while guess != "ComputerScience!":
    print("Wrong password - attempt", attempts, "- probeer opnieuw")
    guess = input("Give the password: ")
    attempts += 1
print("Correct password")