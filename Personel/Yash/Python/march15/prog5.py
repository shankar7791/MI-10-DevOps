# Program 5 : Remove all duplicates words from a given sentence        Examples:        
#         Input : Geeks for Geeks
#         Output : Geeks for        
#         Input : Python is great and Java is also great
#         Output : is also Java Python and great

inp = input("Enter the sentence : ")
lst = inp.split() 
k = [] 
for i in lst: 
    if (inp.count(i)>1 and (i not in k)or inp.count(i)==1): 
        k.append(i) 

print(k)
print(' '.join(k)) 