# Define the nested list
nested_list = [[1, 2], [3, 4], [5, 6]]

# Initialize an empty list to store the flattened elements
flattened_list = []

# Use nested for loops to flatten the nested list
for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)

# Print the flattened list
print("Flattened list:", flattened_list)