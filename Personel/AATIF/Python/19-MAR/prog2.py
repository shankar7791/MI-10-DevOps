'''
    Write a Python program to find a pair with highest product from a given array of integers.
    Examples :
    Input: arr = {1, 2, 3, 4, 7, 0, 8, 4}
    Output: {7,8}
    Input: arr = {0, -1, -2, -4, 5, 0, -6}
    Output: {-4, -6}

'''
def Prod(array, n):
 
    if (n < 2):
        print("Not pairing")
        return
     
    
    a = arr[0]; b = arr[1]
 
    
    for i in range(0, n):
         
        for j in range(i + 1, n):

            if (arr[i] * arr[j] > a * b):
                a = arr[i]; b = arr[j]
 
    print("Pair having maximum product value: {", a, ",", b, "}", end = "")
     
arr = [1, 2, 3, 4, 7, 0, 8, 4]
arr1 = [0, -1, -2, -4, 5, 0, -6]
n = len(arr)
Prod(arr, n)