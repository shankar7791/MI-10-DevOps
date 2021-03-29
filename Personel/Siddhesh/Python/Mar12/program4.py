#Python set to check if string is panagram


import string 
  
def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True

string = input("Enter the string: ")
if(ispangram(string) == True): 
    print("Yes") 
else: 
    print("No") 

    #'THE quick brown fox jumps over the lazy dog' this must be out put

