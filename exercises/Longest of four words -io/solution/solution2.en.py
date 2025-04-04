longestWord = ""
for word in input("Give 4 words, separated by a dash ( - ): ").split("-"):
    if len(word) > len(longestWord):
        longestWord = word
print("The longest of the four words is:", longestWord)