#Remove Duplicate word from sentence 
s = input("Enter Sentence : ")
l = s.split() 
k = [] 
for i in l: 
  
    # If condition is used to store unique string  
     
    if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
        k.append(i)       # k is list name
print(' '.join(k)) 