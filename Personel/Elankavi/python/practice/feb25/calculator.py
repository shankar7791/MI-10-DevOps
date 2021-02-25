
i=2
while(i>0):
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    c=input("+,-,*,/ : ")

    if(c == '+'):
        print(f"The addition of {a} and {b} is : ",a+b)
    elif(c == '-'):
        print(f"THe sub of {a} and {b} is : ",a-b)
    elif(c == '*'):
        print(f"The multiplication of{a} and {b} is : ",a*b)
    elif(c == '/'):
        print(f"The division of {a} and {b} is : ",a/b)
    else:
        print("Enter valid sign")
    d=input("Want to continue again (y/n): ")
    if(d == 'n'):
        i=0
    
