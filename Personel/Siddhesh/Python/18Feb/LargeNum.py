
num1 = int(input("Enter first number ; "))

num2 = int(input("Enter second number : "))

num3 = int(input("Enter third number : "))

if (num1 > num2) and (num1 > num3) :
    lasgest = num1
    print(f"{largest} Is the largest number")

elif (num2 > num1) and (num2 > num3) :
    largest = num2
    print(f"{largest} Is the largest number")

else :
    largest = num3 
    print(f"{largest} Is the largest number")