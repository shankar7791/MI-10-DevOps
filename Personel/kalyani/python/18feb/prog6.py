#Program to check whether a number is divisible by 5 and 11 or not 

a = int(input("Enter the number :"))

if (a % 5 == 0) and (a % 11 == 0) :
    print(f"{a} is divisible by 5 and 11")
else :
    print(f"{a} is not divisible by 5 and 11")
    