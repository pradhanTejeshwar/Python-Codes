principal = int(input("Enter principal amount:"))
time = int(input("Enter duration of loan: "))
interest = int(input("Enter rate of interest: "))
simple_interest = principal*time*(interest/100)
print("Total Interest = ", int(simple_interest))