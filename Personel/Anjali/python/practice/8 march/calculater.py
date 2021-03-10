def cal():
    if ch=='1':
        print(f"Addition {num1+num2}")
    elif ch=='2':
        print(f"Subtraction {num1-num2}")
    elif ch=='3':
        print(f"Multiplication {num1*num2}")
    elif ch=='4':
        print(f"Division {num1/num2}")
    elif ch=='5':
        print(f"Moduls {num1%num2}")
    elif ch=='6':
        print(f"Exponent {num**num2}")
    else:
        print("Invalid choice")
ch=input("""
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Moduls
6.Exponent
Enter the choice   """)
num1=int(input("Enter the number1  "))
num2=int(input("Enter the number2   "))
cal()