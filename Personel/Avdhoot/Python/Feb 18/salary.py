a = int(input("Enter Basic Salary :"))

if a <= 10000 :
    DA = (a * 80) / 100
    HRA = (a * 20) / 100
    Gross_Salary = a + DA + HRA
    print("Gross Salary ", Gross_Salary)

elif a >= 10001 and a <= 20000 :
    DA = (a * 90) / 100
    HRA = (a * 25) / 100
    Gross_Salary = a + DA + HRA
    print("Gross Salary ", Gross_Salary)

elif a >= 20001 :
    DA = (a * 95) / 100
    HRA = (a * 30) / 100
    Gross_Salary = a + DA + HRA
    print("Gross Salary ", Gross_Salary)

else :
    print("Invalid input")
