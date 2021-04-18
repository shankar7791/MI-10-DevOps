'''Write a Python program to find a pair with highest product from a given array of integers.
Examples :
Input: arr[] = {1, 2, 3, 4, 7, 0, 8, 4}
Output: {7,8}
Input: arr[] = {0, -1, -2, -4, 5, 0, -6}
Output: {-4, -6}
'''
import array as arr
import array as arr1

arr = arr.array('i', [1, 2, 3, 4, 7, 0, 8, 4]) 
print ("Array is : ", end =" ") 
for i in range (len(arr)): 
    print (arr[i], end =" ") 
print()

length = len(arr)
a = arr[0]
b = arr[1]
if length < 2:
    print("No Pairs")
else:
    for i in range (0,length):
        for j in range(i+1,length):
            if arr[i] * arr[j] > a * b:
                a = arr[i]
                b = arr[j]
print(a,b)


arr1 = arr1.array('i', [0, -1, -2, -4, 5, 0, -6]) 
print ("Array is : ", end =" ") 
for i in range (len(arr1)): 
    print (arr1[i], end =" ") 
print()

length = len(arr1)
c = arr1[0]
d = arr1[1]
if length < 2:
    print("No Pairs")
else:
    for i in range (0,length):
        for j in range(i+1,length):
            if arr1[i] * arr1[j] > c * d:
                c = arr1[i]
                d = arr1[j]
print(c,d)