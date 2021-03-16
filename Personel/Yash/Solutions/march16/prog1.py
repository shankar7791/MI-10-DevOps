# Program 1: Python program to interchange first and last elements in a list

lst = []
n = int(input("Enter the no of elements is list : "))
for i in range(0,n) :
    inp=int(input())
    lst.append(inp)
print("Before Swapping :\n",lst)
lst[0], lst[-1] = lst[-1], lst[0] 
print("After Swapping :\n",lst) 
