# Program to print duplicates from a list of integers

def Dup(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
  
list1 = [-1, 1, -1, 8] 
print("Duplicate Element in List: ", Dup(list1))