a = int(input("Enter Basic Salary :"))

if a <= 10000 :
    DA = (a * 40) / 100
    HRA = (a * 20) / 100
    Gross_Salary = a + DA + HRA
    print("Gross Salary ", Gross_Salary)

elif a >= 10001 and a <= 20000 :
    DA = (a * 40) / 100
    HRA = (a * 20) / 100
    Gross_Salary = a + DA + HRA
    print("Gross Salary ", Gross_Salary)

elif a >= 20001 :
    DA = (a * 40) / 100
    HRA = (a * 20) / 100
    Gross_Salary = a + DA + HRA
    print("Gross Salary ", Gross_Salary)

else :
    print("Invalid input")