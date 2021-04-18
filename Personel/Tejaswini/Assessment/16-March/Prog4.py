#  Remove all duplicates from a given string in Python

def rmDupli(str): 
    s=set(str) 
    s="".join(s) 
    print("String After removing duplicates:",s)  
      
str=input("Enter the String: ")
rmDupli(str) 


