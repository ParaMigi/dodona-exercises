a = int(input("Give the first number: "))
b = int(input("Give the second number: "))
smallest = min(a, b)
gcd = 1
for n in range(2, smallest+1):
    if (a % n == 0) and (b % n == 0):
        gcd = n
print(f"The greates common divisor of {a} and {b} is {gcd}.")