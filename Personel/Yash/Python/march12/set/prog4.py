# Program 4: Python set to check if string is panagram using set
 
import string 
  
alphabet = set(string.ascii_lowercase) 
print(alphabet)
  
def ispangram(string): 
    return set(string.lower()) >= alphabet 
      
string = input("Enter the string : ") #The quick brown fox jumps over the lazy dog
if(ispangram(string) == True): 
    print("String is panagram") 
else: 
    print("String is not panagram") 