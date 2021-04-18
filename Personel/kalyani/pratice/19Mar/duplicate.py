# Python program to print duplicate element of an array.

arr = [ 1,2,3,4,5,6,7,8,8,3]

print(" duplicate element of given array :")

for i in range ( 0 ,len(arr))

for j in range(i+1 , len(arr))

if(arr[i] = arr[j])

print(arr[j])