item = []
n = int(input("Enter the number of subjects : "))
for i in range(1,n+1) :
    new = int(input("Enter your item "))
    item.append(new)
    ##print(item)
avg = (sum(item)/len(item))
print(item,avg)