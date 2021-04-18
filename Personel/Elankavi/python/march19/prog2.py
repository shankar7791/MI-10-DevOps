# write a program to find the pair with highest product from a given array of integer :


def max():
    
    arr=[12,3,4,56,6,8]
    n=len(arr)
    a = arr[0] ; b = arr[1]
    if n<2:
        print("There is no pair of numbers")
    else:
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i] * arr[j] > a*b:
                    a=arr[i] ; b=arr[j]
    print(a,b)
max()




