
# Write a Python program to add two positive integers without using the '+' operator

x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
def Add(x, y):
    while (y != 0):
        c = x & y
        x = x ^ y
        y = c << 1
     
    return x
print("Addition of two numbers = ",Add(x, y))