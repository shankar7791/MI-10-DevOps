# Write a Python program to find a pair with highest product from a given array of integers.

def pro(arr, n):
 
    if (n < 2):
        print("No pairs exists")
        return
     
    a = arr[0]; b = arr[1]
 
    
    for i in range(0, n):
         
        for j in range(i + 1, n):
            if (arr[i] * arr[j] > a * b):
                a = arr[i]; b = arr[j]
 
    print("Max product pair is {", a, ",", b, "}",
                                          sep = "")
     
 
N=int(input('enter number of elements in array')) #take the size

arr=list(map(int, input().split(' ')[:N]))
n=len(arr)
print(pro(arr,n))