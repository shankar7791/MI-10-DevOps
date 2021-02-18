Number1 = int(input("enter the number1 : "))
Number2 = int(input("enter the number2 : "))
Number3 = int(input("enter the number3 : "))

if Number1 >= Number2 and Number1 >= Number3 :
    print(f"{Number1} is largest")
elif Number2 >= Number1 and Number2 >= Number3 :
    print(f"{Number2} is largest")
else:
    print(f"{Number3} is largest")