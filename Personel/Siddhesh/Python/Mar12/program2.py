#Check whether a given string is Heterogram or not

def heterogram(input): 
  
     alphabets = [ ch for ch in input if ( ord(ch) >= ord('a') and ord(ch) <= ord('z') )] 
  
     if len(set(alphabets))==len(alphabets): 
         print ('Yes') 
     else: 
         print ('No') 

input = input("Enter the string : ")
heterogram(input)


