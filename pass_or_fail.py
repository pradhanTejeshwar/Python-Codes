#WAP to determine a student’s final grade and indicate whether they are passing or failing. The final grade is calculated as the average of marks of four subjects.
sub1=int(input("Enter marks of subject 1: "))
sub2=int(input("Enter marks of subject 2: "))
sub3=int(input("Enter marks of subject 3: "))
sub4=int(input("Enter marks of subject 4: "))
avg_marks = (sub1 + sub2 + sub3 + sub4)/4

print('Your Grade is: ', avg_marks)

if(avg_marks > 40) :
    print("Congratulation You have Passed")
else :
    print("Sorry You Failed")