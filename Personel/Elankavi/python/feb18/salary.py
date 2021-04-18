#program to input basic salary of an employee and calculate gross salary

basic_salary = float(input("Enter the salary of an employee : "))
if(basic_salary <= 10000):
    hra = basic_salary  * 0.2
    da = basic_salary  * 0.8
elif(basic_salary >=10001 and basic_salary <=20000):
    hra = basic_salary  * 0.25
    da = basic_salary  * 0.9
elif(basic_salary >20000):
    hra = basic_salary  * 0.3
    da = basic_salary  * 0.95

gross = basic_salary  + hra + da
print("Gross salary of an employee : " ,gross)