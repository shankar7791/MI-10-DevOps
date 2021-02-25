#Python program to add two positive integers without using the '+' operator

a=int(input("Enter a :"))
b=int(input("Enter b :"))

while(b != 0):

    c = a & b

    a ^= b

    b = c << 1

print("addition is :", a)