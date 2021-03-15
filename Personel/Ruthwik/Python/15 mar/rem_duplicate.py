# Remove all duplicates words from a given sentence
#         Examples:
#         Input : Geeks for Geeks
#         Output : Geeks for
#         Input : Python is great and Java is also great
#         Output : is also Java Python and great
 

s = "Python is great and Java is also great"
l = s.split() 
k = [] 
for i in l: 
  
    # If condition is used to store unique string  
    # in another list 'k'  
    if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
        k.append(i) 
print(' '.join(k)) 