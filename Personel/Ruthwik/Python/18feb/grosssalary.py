#Program to input basic salary of an employee and calculate gross salary according to given conditions.

bas = int(input("Enter basic salary :"))

if bas <= 10000 :
    hra = bas * 0.2
    da = bas * 0.8
    gross = bas+hra+da
    print(f"The gross salary is {gross} at {bas} basic salary")
elif (bas >= 10001) and (bas <= 20000) :
    hra = bas * 0.25
    da = bas * 0.9
    gross = bas+hra+da
    print(f"The gross salary is {gross} at {bas} basic salary")
else :
    if bas >= 20001 :
        hra = bas * 0.3
        da = bas * 0.95
        gross = bas+hra+da
        print(f"The gross salary is {gross} at {bas} basic salary")
