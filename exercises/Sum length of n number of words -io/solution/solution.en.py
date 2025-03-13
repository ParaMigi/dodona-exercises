number_of_words = int(input("How many words do you want to say? "))
sum = 0
for i in range(number_of_words):
    word = input(f"Give word number {i+1}: ")
    sum += len(word)
print(f"The sum of the letters in all words is {sum}.")