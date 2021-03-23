# Creating arrays

import array as arr
a = arr.array('d', [1.1, 3.5, 4.5])
print(a)

# accessing array elements

a = arr.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

# array slicing

n = [2, 5, 62, 5, 42, 52, 48, 5]
n_array = arr.array('i', n)

print(n_array[2:5]) 
print(n_array[:-5]) 
print(n_array[5:])  
print(n_array[:])   

# changing and adding elements

n_array[2:5] = arr.array('i', [4, 6, 8])   
print(n_array) 

# Reverse the numbers 

b = arr.array('i',[1,2,3,4,5,6,7,8,9])
print("Original String : ")

for i in b :
    print(i,end=" ")
print("\nReverse String : ")
b.reverse()
for i in b :
    print(i,end=" ")
print("\n")


# number of occurrences of a specified element in an array


c = arr.array('i',[1,2,3,4,5,6,7,8,9,8,7,6,5,6,5,8,9,2,4,3,2,1,0,0])
print("Original String : ")
for i in c :
    print(i,end=" ")
print()
n = int(input("Enter the element which you want to count : "))
print(f"The count of {n} is : {c.count(n)}") 


# Write a Python program to convert an array to an array of machine values and return the bytes representation.

from array import *
print("Bytes to String: ")
x = array('b', [114, 117, 116, 104, 119, 105, 107])
s = x.tobytes()
print(s)