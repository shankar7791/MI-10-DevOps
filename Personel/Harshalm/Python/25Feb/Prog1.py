#Write a Python program to add two positive integers without using the '+' operator.

num1 = int(input("Enter first number :-"))
num2 = int(input("Enter second number :-"))

while num2 != 0 :
    sum = num1 & num2
    num1 ^= num2
    num2 = sum << 1
print("Adiitionn is :-", num1)

