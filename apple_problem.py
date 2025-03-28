n = int(input('Enter the number of Children : '))

lst = []

lst = list(map(int, input("Enter the values here").split()))

avg = sum(lst)/len(lst)
c=0
print(f'Avg : {avg}')
for i in range(n-1) :
    while (lst[i] > avg) :
        if i == 0 :
            l = n
        else :
            l = i-1
        if(lst[i] > lst[l] and lst[l] < avg) :
            lst[i]-=1
            lst[l]+=1
            c+=1
        i+=1

'''if(lst[i] > lst[r]) :
            lst[i]-=1
            lst[r]+=1
            c+=1
'''

'''        if(lst[i] > lst[l]) :
            lst[i]-=1
            lst[l]+=1
            c+=1
        i-=1
        if i == n :
            r = 0
        if(lst[i] > lst[r]) :
            
            lst[i]-=1
            lst[r]+=1
            if i == n + 1 :
                i = 0
            c+=1
'''

print(c)
print(lst)