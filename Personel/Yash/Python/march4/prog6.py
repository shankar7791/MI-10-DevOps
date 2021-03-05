# Program 6 : Write a Python function to check whether a string is a pangram or not.

def checkPangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
    return True

# string = 'the quick brown fox jumps over the lazy dog' 
string=input("Enter the string : ")
if(checkPangram(string) == True): 
    print("Entered string is a pangram") 
else: 
    print("Entered string is not a pangram") 