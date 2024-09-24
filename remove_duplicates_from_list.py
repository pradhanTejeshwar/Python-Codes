#data_list = [1,2,7,4,3,4,2,7,5,6,2]
data_list = [1,2,4,2,1,3]
data_list.sort()
print(data_list)
for i in data_list :
    if (data_list[i] == data_list[i+1]) :
        data_list.remove(i)
print(data_list)

'''
unique = []
for i in data_list :
    if i not in unique :
        unique.append(i)
print(unique)
print(data_list)
'''