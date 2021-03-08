#simple calculator 1. Addition 2. sub 3. multi 4. div  5.moduls 6. exponent
def calculator():
   
    a=int(input(f"Enter the first number : "))
    b=int(input("Enter the second numnber : "))
    c=input("""
    1.Addition
    2.subtract
    3.multiply
    4.division
    5.moduls.
    6.exponent
    Enter your choice : """)
    if(c=='1'):
        print("The solution is : ",a+b)
    elif(c=='2'):
        print("The solution is : ",a-b)
    elif(c=='3'):
        print("The solution is : ",a*b)
    elif(c=='4'):
        print("The solution is : ",a/b)
    elif(c=='5'):
        print("The solution is : ",a%b)
    elif(c=='6'):
        print("The solution is : ",a**b)
    else:
        print("Enter the valid input")
        print()
        calculator()
calculator()