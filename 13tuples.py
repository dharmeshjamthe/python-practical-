# Define a tuple of integers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Print the first and last elements of the tuple
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Calculate the middle index
middle_index = len(numbers) // 2

# Print the middle element(s)
if len(numbers) % 2 == 0:
    print("Middle elements:", numbers[middle_index - 1], numbers[middle_index])
else:
    print("Middle element:", numbers[middle_index])