def Remove(input_set): 
    while input_set: 
        input_set.pop() 
        print(input_set) 

input_set = set((1,1,2,3,3,4,4,5,6,7,8,8,8,8,99)) 
print(input_set)
Remove(input_set)  