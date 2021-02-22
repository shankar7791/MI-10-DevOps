# Prog 7 : Write a program to input basic salary of an employee and calculate gross salary according to given conditions.
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary is between 10001 to 20000 : HRA = 25%, DA = 90%
# Basic Salary >= 20001 : HRA = 30%, DA = 95%" (edited)

Basic_Salary = int(input("Enter Basic Salary :"))

DA = (Basic_Salary * 40) / 100
HRA = (Basic_Salary * 20) / 100
Gross_Salary = Basic_Salary + DA + HRA

print("\n\nDearness Allowance 40 % of Basic_Salary :", DA)
print("House Rent 20 % of Basic_Salary :", HRA)
print("Gross Salary :", Gross_Salary)
