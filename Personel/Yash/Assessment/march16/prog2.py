# Program 2 : Program to print duplicates from a list of integers 

lst = [1,2,3,4,1,2,5]  
     
print("Duplicate elements in given array: ");     
for i in range(0, len(lst)):    
    for j in range(i+1, len(lst)):    
        if(lst[i] == lst[j]):    
            print(lst[i])