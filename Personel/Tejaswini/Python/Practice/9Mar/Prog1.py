#Write a program to find the last occurence of the letter 

def lastIndex(str, x): 
    index = -1
    for i in range(0, len(str)): 
        if str[i] == x: 
            index = i 
    return index 
  

str = input("Enter The String : " ) 
x = input("Enter Character : ")
  
index = flastIndex(str, x) 
  
if index == -1: 
    print("Character not found") 
else: 
    print("Last index is", index) 