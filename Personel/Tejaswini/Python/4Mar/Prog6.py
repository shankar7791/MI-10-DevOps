#Check whether a string is pangram or not

import string

def pangram(str1):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
        if char in str1.lower():
            return True
        else:
            return False
str1= input("Enter the string: ")
if pangram(str1)==True:
    print(f"The String is pangram:{str1}")
else:
    print(f"The String is pangram:{str1}")