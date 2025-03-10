number = int(input("Give a number: "))

isPrime = True

for i in range(2, number):
    if number % i == 0:
        isPrime = False

if isPrime:
    print(number, "is prime")
else:
    print(number, "is not prime")