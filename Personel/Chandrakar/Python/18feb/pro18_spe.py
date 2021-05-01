#Write a program to check  entered input is  alphabet digit or special character
a = input("enter character : ")
if((a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z')): 
    print(f"{a} is an Alphabet") 
elif(a >= '0' and a <= '9'):
    print(f"{a} is a Digit")
else:
    print(f"{a}is a Special Character")