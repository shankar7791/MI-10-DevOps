# Remove items from Set until set not become empty set
def empty(set2): 
    while set2: 
        set2.pop() 
        print(set2) 
set1 = set([1, 4, 6, 5, 8, 9]) 
empty(set1)