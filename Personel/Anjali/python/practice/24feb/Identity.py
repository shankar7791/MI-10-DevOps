#Identity operators

num1=int(input("Enter the number"))
num2=int(input("Enter the number"))

if (num1 is num2):
    print(f"{num1} and {num2} is same")
elif (num1 is not num2):
    print(f"{num1} and {num2} is not same")