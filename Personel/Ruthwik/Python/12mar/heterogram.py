# Check whether a given string is Heterogram or not

def heterogram_chk(string): 
   
     alphabets = [ ch for ch in string if ( ord(ch) >= ord('a') and ord(ch) <= ord('z') )] 
  
     # convert list of alphabets into set and compare lengths
      
     if len(set(alphabets))==len(alphabets): 
         print ('It is a Heterogram') 
     else: 
         print ('It is not a Heterogram') 

s = input('Enter a string : ')

heterogram_chk(s)