# Remove all duplicates from a given string in Python 

def rem_dupli(s):
    l = "".join(set(s))
    k = [] 
    for i in l: 
  
    # If condition is used to store unique string  
    # in another list 'k'  
        if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
            k.append(i) 
    print(' '.join(k)) 


string=input('Enter a string : ')

rem_dupli(string)