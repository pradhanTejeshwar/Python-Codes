numbers = [7,5,9,2,8,4,3]
lar = 0
sml = 9
for i in numbers :
    if i > lar :
        lar = i
    if i < sml :
        sml = i
print(f'Largest Number in the List is : {lar}')
print(f'Smallest Number in the List is : {sml}')
print(numbers)