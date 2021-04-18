#Python set to check if string is panagram

def panagram(string): 

    string = string.lower()
    string = set(string)

    alphabets = [ ch for ch in string if ( ord(ch) in range(ord('a'), ord('z')+1)) ] 

    if len(alphabets) == 26: 
        print ('it is a pangram') 
    else: 
        print ('it is not a pangram') 

s = input("Enter a string : ")

panagram(s) 