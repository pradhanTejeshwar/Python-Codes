numbers = [2,2,2,2,5]
for i in numbers :
    for j in range(i) :
        print('x', end="")
    print('')

for i in numbers :
    output = ''
    for j in range(i) :
        output += 'x'
    print(output)