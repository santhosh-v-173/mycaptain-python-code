list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

result = []
for i in list1:
    if i > 0:
        result.append(str(i))

print(', '.join(result))
        
result.clear()

for i in list2:
    if i > 0:
        result.append(i)

print(result)
