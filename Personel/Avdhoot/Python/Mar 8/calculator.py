#Python program to create calculator

print("Enter your Choice: ")
print("1. Addition ")
print("2. Substraction ")
print("3. Multiplication ")
print("4. Division ")
print("5. Modulus ")
print("6. Exponent ")

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
def mod(a,b):
    return a % b
def fdiv(a,b):
    return a // b

ip = int(input("Enter your Choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if ip == 1:
    print(add(a,b))
elif ip == 2:
    print(sub(a,b))
elif ip == 3:
    print(mul(a,b))
elif ip == 4:
    print(div(a,b))
elif ip == 5:
    print(mod(a,b))
elif ip == 6:
    print(fdiv(a,b))
else:
    print("Invalid Input ")