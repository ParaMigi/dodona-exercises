wordOrPhrase = input("Give a word or phrase: ")
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxz"
nVowels = 0
nConsonants = 0
for char in phrase:
    if char in vowels:
        nVowels += 1
    elif char in consonants:
        nConsonants += 1
print("Vowels:", nVowels)
print("Consonants:", nConsonants)