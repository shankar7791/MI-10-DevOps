a = float(input("Enter the salary of an employee : "))
if(a<= 10000):
    hra = a * 0.2
    da = a * 0.8
elif(a>=10001 and a<=20000):
    hra = a * 0.25
    da = a * 0.9
elif(a>20000):
    hra = a * 0.3
    da = a * 0.95

gross = a + hra + da
print("Gross salary of an employee : " ,gross)