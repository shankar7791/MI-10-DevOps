# Write a Python function to check whether a string is a pangram or not.


import string

def ispangram(str) :
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabets :
        if i not in str.lower():
            return False

    return True

string = input("Enter the string :-")
if ispangram(string) == True :
    print("yes")

else :
    print("no")

