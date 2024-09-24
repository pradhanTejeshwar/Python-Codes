months_dic = [('january',1),('february',2),('march',3),('april',4),('may',5),('june',6),('july',7),('august',8),
              ('september',9),('october',10),('november',11),('december',12)]

def shelf_months(festival_month):
    for name,num in months_dic:
        if name == festival_month:
            month_num = num
    month_list=[]
    for i in range(month_num - 1 , month_num + 2):
        if i == 13: i = 1
        if i == 0 : i = 12
        month_list.append(months_dic[i-1][0])
    print('You have to display the products for the months',end=' : ')
    for x in month_list:
        print(x,end=' , ')
    
if __name__ == '__main__':
    festival_month = input("Enter the next festival month: ").lower()
    shelf_months(festival_month)