# Program 3: Remove items from Set until set not become empty set 

def Remove(input_set): 
    while input_set: 
        input_set.pop() 
        print(input_set) 
   
input_set = set((9,1,2,3,4,5,6,7,8,9,1,2,4,5,3,6,9,8,7)) 
print(input_set)
Remove(input_set) 