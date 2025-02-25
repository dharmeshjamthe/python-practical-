strings = ["apple", "banana", "cherry", "date", "elderberry"]

search_string = "cherry"

found = False

for string in strings:
    if string == search_string:
        found = True
        break

# Print the result
if found:
    print("Found")
else:
    print("Not Found")