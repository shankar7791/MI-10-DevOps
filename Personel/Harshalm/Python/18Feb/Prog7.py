#Basic salary

BasicSalary = int(input("Enter the Basic Salary :- "))

DA = (BasicSalary * 40) / 100
HRA = (BasicSalary * 20) / 100
GrossSalary = BasicSalary + DA + HRA

print("Allowance 40% of Basic Salary :- ", DA)
print("House Rent 20% of Basic  salary :", HRA)
print("GrossSalary :- ", GrossSalary)