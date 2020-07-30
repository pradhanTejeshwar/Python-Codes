#WAP that reads two numbers and an arithmetic operator and displays the result.
num1 = float(input("Enter first number(Non-Negative): "))
num2 = float(input("Enter second number(Non-Negative): "))
operator = input("Enter operator ( +  - * / %) : ")

if(operator == "+") :
    print("{:.2f}".format(num1 + num2))
elif(operator == "*") :
    print("{:.2f}".format(num1 * num2))
elif(operator == "-") :
    print("{:.2f}".format(num1 - num2))
elif(operator == "/") :
    print("{:.2f}".format(num1 / num2))
elif(operator == "%") :
    print("{:.2f}".format(num1 % num2))
else :
    print("Operation Failed ! Choose again from Options given")