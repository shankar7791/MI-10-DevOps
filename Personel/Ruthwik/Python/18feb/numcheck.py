# Python program to check number is positive, negative or zero

a = int(input("Enter the number :"))

if a < 0 :
    print(f"{a} is a negative number")
elif a == 0 :
    print(f"{a} is zero ")
else :
    print(f"{a} is a positive number")