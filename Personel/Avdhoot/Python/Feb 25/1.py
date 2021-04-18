#Write a Python program to add two positive integers without using the '+' operator

a=int(input("Enter the number for a: "))
b=int(input("Enter the number for b: "))
while(b != 0):
    c=a&b       #and operator
    a=a^b       #Xor operator
    b=c<<1      #c is shifted by one so that adding it to x gives the required sum

print(a)