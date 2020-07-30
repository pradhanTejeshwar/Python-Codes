num = int(input("Enter the two digit number: "))
rev = 0
while(num > 0) : 
    digit = num % 10
    rev = (rev * 10) + digit
    num = num//10
print("Reverse of the given number is: ", rev)