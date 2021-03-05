# Program 1 : Write a Python function to sum all the numbers in a list. 

def sum_list(lst):
    sum = 0
    for x in lst:
        sum += x
    return sum

lst = [] 
 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    lstInput = int(input(f"Enter the element {i+1} : ")) 
    lst.append(lstInput)
      
print(lst) 
print("Sum of all numbers in a list => ",sum_list(lst))