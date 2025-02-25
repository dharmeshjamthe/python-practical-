numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)

print("Even numbers using for loop and if statement:", even)

# Using list comprehension
even_numbers_comprehension = [number for number in numbers if number % 2 == 0]

print("Even numbers using list comprehension:", even_numbers_comprehension)