
# Find length of a string in python using for loop

def Len(str): 
    counter = 0    
    for i in str: 
        counter += 1
    return counter 
  
str = str(input("Enter A String : "))
print(Len(str)) 