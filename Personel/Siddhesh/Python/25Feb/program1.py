#Write a Python program to add two positive integers without using the '+' operator.

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
while num2 !=0:
        count=num1 & num2
        num1=num1^num2
        num2=count << 1
        
print("Sum of two numbers are",num1)