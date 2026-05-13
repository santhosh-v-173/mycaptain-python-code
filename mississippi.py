def most_frequent(word):
    result = {}

    for i in word:
        result[i] = word.count(i)

    sorted_result = sorted(result.items(),key=lambda x: x[1], reverse=True)
    return sorted_result
    

result = most_frequent("Mississippi")

for key,value in result:
        print(key+" = 0" +str(value))