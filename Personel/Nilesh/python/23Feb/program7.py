#Write a Python program that accepts a string and calculate the number of digits and letters.
string = (input("enter the string : "))
a = 0
b = 0
for i in string :
    if(i.isdigit()):
        a = a + 1
    b = b + 1
print("the number of digit are : ")
print(a)
print("the number of letters are : ")
print(b)