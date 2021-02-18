Basic_Sal= float(input("Enter Basic Salary :"))

if Basic_Sal <= 10000:
    HRA = (Basic_Sal * 20) / 100
    DA = (Basic_Sal * 80) / 100
    
    Gross_Sal = Basic_Sal + DA + HRA
    print(f"\nGross_Salry is {Gross_Sal},\non {Basic_Sal} Basic Salry")

elif Basic_Sal >= 10001 and Basic_Sal <= 20000:
    HRA = (Basic_Sal * 25) / 100
    DA = (Basic_Sal * 90) / 100
    
    Gross_Sal = Basic_Sal + DA + HRA
    print(f"\nGross_Salry is {Gross_Sal},\non {Basic_Sal} Basic Salry")

else:
    HRA = (Basic_Sal * 30) / 100
    DA = (Basic_Sal * 95) / 100
    
    Gross_Sal = Basic_Sal + DA + HRA
    print(f"\nGross_Salry is {Gross_Sal},\non {Basic_Sal} Basic Salry")
