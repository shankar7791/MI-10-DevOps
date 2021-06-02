#linear searching program
def linear(arr):
    val = 0       #take on varible
    for ind in range(len(arr)):  
        print(ind)      
        if n ==arr[ind]:          #checking the index
            val = 1
    
            print(f"Element found in index  = {ind}")
    if val ==0:
        print(f"{n} This element not present in array")             

arr = [10,50,30,70,80,60,20,90,40]                # A variable list is taken as an array
print(range(len(arr)))
n = int(input(f"{arr}\nChoise the search of this array ="))
linear(arr)    #call linear function

