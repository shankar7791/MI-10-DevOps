# Python Program to check character is Alphabet Digit or Special Character


character = input("Please Enter Your Own Character : ")

if((character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z')): 
    print(f"\n{character}\nThe Given character is an Alphabet") 
elif(character >= '0' and character <= '9'):
    print(f"\n{character}\nThe Given character is a Digit")
else:
    print(f"\n{character}\nThe Given character is a Special character")