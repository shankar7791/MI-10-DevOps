#Write a Python function to check whether a string is a pangram or not.
import string 
  
def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True
      
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True): 
    print("Yes") 
else: 
    print("No") 