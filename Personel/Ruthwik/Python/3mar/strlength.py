def findLen(str): 
    counter = 0    
    for c in str: 
        counter += 1
    return counter 
  
  
str = input("enter a string : ")
print(findLen(str)) 