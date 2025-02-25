number = int(input("Enter a number: "))

if number < 0:
    print("Error: The number is negative.")
else:
    while number >= 0:
        print(number)
        number -= 1