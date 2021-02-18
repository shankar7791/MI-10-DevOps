basicsalary=int(input("Enter salary"))

if basicsalary<=1000 :
    DA = (basicsalary * 40) / 100
    HRA = (basicsalary * 20) / 100
    Gross_Salary = basicsalary + DA + HRA
    print(f"{Gross_Salary} is a Gross_Salary ")


elif basicsalary>=10001 and basicsalary<=20000 :
    DA = (basicsalary * 90) / 100
    HRA = (basicsalary * 25) / 100
    Gross_Salary = basicsalary + DA + HRA
    print(f"{Gross_Salary} is a Gross_Salary ")

elif basicsalary>=20001 :
    DA = (basicsalary * 40) / 100
    HRA = (basicsalary * 20) / 100
    Gross_Salary = basicsalary + DA + HRA
    print(f"{Gross_Salary} is a Gross_Salary ")

else :
    print("Invalid")