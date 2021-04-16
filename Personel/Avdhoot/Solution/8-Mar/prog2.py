#Check if Binary representation is Palindrome in Python

a = int(input("Enter a number: "))
b = int(bin(a)[2:])

c = str(b)[::-1]
d = int(c)

if b == d :
    print("True")
    print("Binary representtion of " + f"{a} is " + f"{b} " + "which is palindrome as well")
else :
    print("False")
    print("Binary representtion of " + f"{a} is " + f"{b} " + "which is not palindrome")