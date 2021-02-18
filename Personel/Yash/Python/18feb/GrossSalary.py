'''Prog 7 : Write a C program to input basic salary of an employee and calculate gross salary according to given conditions.
    Basic Salary <= 10000 : HRA = 20%, DA = 80%
    Basic Salary is between 10001 to 20000 : HRA = 25%, DA = 90%
    Basic Salary >= 20001 : HRA = 30%, DA = 95%" '''

Basic_Salary = float(input("Enter Basic Salary of an employee : "))

if (Basic_Salary<=10000) :
    HRA = (20*Basic_Salary) / 100 
    DA = (80*Basic_Salary) / 100
elif (Basic_Salary>=10001 and Basic_Salary<=20000) :
    HRA = (25*Basic_Salary) / 100 
    DA = (80*Basic_Salary) / 100
else :
    HRA = (30*Basic_Salary) / 100 
    DA = (95*Basic_Salary) / 100

Gross_Salary = Basic_Salary + HRA + DA

print(f"Gross salary of an employee is {Gross_Salary}")