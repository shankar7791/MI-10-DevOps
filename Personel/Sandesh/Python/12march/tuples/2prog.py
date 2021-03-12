
#Convert a list of characters into a string

def convert(s): 
  
    str = "" 

    return(str.join(s)) 
         
s = list(input("Enter a List : "))
print(tuple(s))
print(convert(s))
print("the Converted list into a string : ",convert(s))