number = smallest = largest = int(input("Give a number"))
while number != 0:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
    number = int(input("Give another number"))
print(f"The smallest of the numbers is {smallest}, while the largest is {largest}.")