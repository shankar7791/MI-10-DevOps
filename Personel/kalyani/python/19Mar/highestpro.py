# Write a Python program to find a pair with highest product from a given array of integers.


def highproir(arr):
    
    n=len(arr)
    a = arr[0] ; b = arr[1]
    if n<2:
        print("There is no pair of numbers")
    else:
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i] * arr[j] > a*b:
                    a=arr[i] ; b=arr[j]
    print("{",a,",",b,"}")
arr1=[12,3,4,56,6,8]
highproir(arr1)
arr2=[0,-2,-1,-3,-4,5,-6]
highproir(arr2)