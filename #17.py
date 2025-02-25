# Define the list of numbers
numbers = [4, 2, 7, 3, 2, 8, 1, 4, 9, 6, 3, 5, 7]

# Remove duplicates by converting the list to a set
unique_numbers = list(set(numbers))

# Sort the list in ascending order
unique_numbers.sort()

# Print the result
print("List after removing duplicates and sorting:", unique_numbers)