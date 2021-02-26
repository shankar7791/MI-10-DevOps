#Write a Python program to add two positive integers without using the '+' operator.
num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))

def add(num1,num2):
    while(num2 != 0):
        sum = num1 & num2
        num1 = num1 ^ num2
        num2 = sum << 1
    return num1
print("sum of two integers is : ",add(num1,num2))
