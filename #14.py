# Define the list of integers
numbers = [1, 2, 3, 4, 5, 2, 2, 6, 7, 8, 2, 9, 10]

# Define the specific number to count
specific_number = 2

# Initialize the count
count = 0

# Use a for loop and if statement to count occurrences
for number in numbers:
    if number == specific_number:
        count += 1

# Print the result
print(f"The number {specific_number} appears {count} times in the list.")