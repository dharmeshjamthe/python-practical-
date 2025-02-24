a = []
for i in range(1, 6):
    a.append(i)
    
another_list = [6, 7, 8, 9, 10]
a.extend(another_list)

print("Final list:", a)