word1, word2, word3, word4 = input("Give 4 words, separated by a dash ( - ): ").split("-")
longestWord = word1
if len(word2) > len(longestWord):
    longestWord = word2
if len(word3) > len(longestWord):
    longestWord = word3
if len(word4) > len(longestWord):
    longestWord = word4
print("The longest of the four words is:", longestWord)