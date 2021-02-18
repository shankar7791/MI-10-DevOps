# Python Program to check input is Alphabet Digit or Special Character
ch = input("Enter the character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print(f"{ch} is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print(f"{ch} is a Digit")
else:
    print(f"{ch} is a Special Character")