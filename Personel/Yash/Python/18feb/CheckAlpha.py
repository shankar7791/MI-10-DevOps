#Prog 6 : Write a program to check  entered input is  alphabet digit or special character

ch = input("Enter the Character : ")
if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print(f"The Entered Character {ch} is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print(f"The Entered Character {ch} is a Digit")
else:
    print(f"The Entered Character {ch} is a Special Character")