#Write a Python program to add two positive integers without using the '+' operator.
a = int(input("enter the number : "))
b = int(input("enter the number : "))
def add(a,b) :
    while b != 0 :
        data = a & b
        a = a ^ b
        b = data << 1
    return a              
print("sum of two number :",add(a,b))    