#Write a Python function to check whether a string is a pangram or not.


import string
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True
# main
string = 'The five boxing wizards jump quickly.'
if(ispangram(string) == True):
   print("Yes")
else:
   print("No")