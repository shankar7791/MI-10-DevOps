#Remove items from Set until set not become empty set

def Remove(set1): 
    while set1: 
        set1.pop() 
        print(set1) 
  
set1 = set([1,2,4,8,20,21,21,44,2,7]) 
Remove(set1) 