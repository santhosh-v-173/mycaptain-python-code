word = "Mississippi"
result = {}

for i in word:
    result[i] = word.count(i)

sorted_result = sorted(result.items(),key=lambda x: x[1], reverse=True)

for key,value in sorted_result:
    print(key+" = 0"+str(value))