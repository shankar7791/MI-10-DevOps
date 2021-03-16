#Program to print duplicates from a list of integers 

li=[int(x) for x in input("Enter List: ").split()]
def dupli(li): 
    l= len(li) 
    li2 = [] 
    for i in range(l): 
        k = i + 1
        for j in range(k, l): 
            if li[i] == li[j] and li[i] not in li2: 
                li2.append(li[i]) 
    return li2 
  
print (dupli(li))