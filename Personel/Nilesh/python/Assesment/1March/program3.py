#write a program to check string is palindrome or not.
string = str(input("enter the strig : "))

if string == string[::-1]:
    print("string is palindrome")
else:
    print("string is not a palindrome")