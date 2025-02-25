numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total_sum_loop = 0
for number in numbers:
    total_sum_loop += number

print("Sum of all numbers using for loop:", total_sum_loop)

# Using the built-in sum() function
total_sum_builtin = sum(numbers)

print("Sum of all numbers using sum() function:", total_sum_builtin)