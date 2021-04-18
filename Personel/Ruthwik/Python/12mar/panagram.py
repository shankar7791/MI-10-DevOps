# Python set to check if string is panagram

def pangram_chk(string): 
    
    string = string.lower()
    string = set(string)

    alphabets = [ ch for ch in string if ( ord(ch) in range(ord('a'), ord('z')+1)) ] 
  
     # convert list of alphabets into set and compare lengths
      
    if len(alphabets) == 26: 
        print ('It is a pangram') 
    else: 
        print ('It is not a pangram') 

s = input('Enter a string : ')

pangram_chk(s)