def most_frequent(string):
    value = dict()
    for key in string:
        if key not in value:
            value[key] = 1
        else:
            value[key] += 1
    return sorted(value.items(), key=lambda x: x[1], reverse=True)

 
print(most_frequent(input('Enter a Word : ')))