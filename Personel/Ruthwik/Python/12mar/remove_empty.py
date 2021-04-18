# Remove empty tuples from a list

def rem_empty(tuples): 
    tuples = [t for t in tuples if t] 
    return tuples


t = list(tuple(map(str,input().split())) for r in range(int(input('enter no of rows : ')))) 
print(t) 

print(rem_empty(t))
 
