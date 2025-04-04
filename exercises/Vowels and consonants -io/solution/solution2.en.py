wordOrPhrase = input("Give a word or phrase: ")
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxz"
nVowels = 0
nConsonants = 0
for char in wordOrPhrase:
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        nVowels += 1
    elif (char == "b" or char == "c" or char == "d" or char == "f" or char == "g" or char == "h" or char == "j" or char == "k" or char == "l" or char == "m" or char == "n" or char == "p" or char == "q" or char == "r" or char == "s" or char == "t" or char == "v" or char == "w" or char == "x" or char == "z"):
        nConsonants += 1
print("Vowels:", nVowels)
print("Consonants:", nConsonants)