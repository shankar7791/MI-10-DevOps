salary = int(input("Enter Basic Salary :"))

if salary <= 10000 :
    HRA = (salary * 20) / 100
    DA = (salary * 80) / 100
    Gross_Salary = salary + HRA + DA
    print(f"\n{Gross_Salary}\nGross Salary ")

elif salary >= 10001 and salary <= 20000 :
    HRA = (salary * 25) / 100
    DA = (salary * 90) / 100
    Gross_Salary = salary + HRA + DA
    print(f"\n{Gross_Salary}\nGross Salary ")

elif salary >= 20001 :
    HRA = (salary * 30) / 100
    DA = (salary * 95) / 100
    Gross_Salary = salary + HRA + DA
    print(f"\n{Gross_Salary}\nGross Salary ")

else :
    print("Invalid salary") 