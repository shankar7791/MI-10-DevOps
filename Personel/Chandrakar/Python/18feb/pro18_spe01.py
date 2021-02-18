# Write a program to input basic salary of an employee and calculate gross salary according to given conditions.
Basic_Salary = int(input("Enter basic salary :"))
if Basic_Salary <= 10000 :
     DA = (Basic_Salary * 80) / 100
     HRA = (Basic_Salary * 20) / 100
     Gross_Salary = Basic_Salary + DA + HRA
     print(f"{Gross_Salary} is Gross_Salary ")
elif Basic_Salary <= 20000 : 
     DA = (Basic_Salary * 90) / 100
     HRA = (Basic_Salary * 25) / 100
     Gross_Salary = Basic_Salary + DA + HRA
     print(f"{Gross_Salary} is Gross_Salary ")
elif Basic_Salary >= 20000     :
     DA = (Basic_Salary * 95) / 100
     HRA = (Basic_Salary * 30) / 100
     Gross_Salary = Basic_Salary + DA + HRA
     print(f"{Gross_Salary} is Gross_Salary ")
else :
         print("not determind  is Gross_Salary ")