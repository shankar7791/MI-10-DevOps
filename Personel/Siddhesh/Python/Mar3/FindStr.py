def findLen(str): 
    
    str=str(input("Enter the string: "))

    counter = 0    
    for i in str: 
        counter += 1
    return counter 
  

print(findLen(str)) 

