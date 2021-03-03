#Find length of a string in python using for loop

def len_str(str): 
    count = 0    
    for i in str: 
        count += 1
    return count 
  
  
str = "nilesh"
print(len_str(str)) 
