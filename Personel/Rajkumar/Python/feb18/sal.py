BS = float(input("Enter Basic Salary of employee : "))
if (BS<=10000) :
    HRA = (20*BS) / 100 
    DA = (80*BS) / 100
    GS = BS + HRA + DA
    print(f"Gross salary of employee is {GS}")
elif (BS>=10001 and BS<=20000) :
    HRA = (25*BS) / 100 
    DA = (80*BS) / 100
    GS = BS + HRA + DA
    print(f"Gross salary of employee is {GS}")
else:
    HRA = (30*BS) / 100 
    DA = (95*BS) / 100
    GS = BS + HRA + DA
    print(f"Gross salary of employee is {GS}")    