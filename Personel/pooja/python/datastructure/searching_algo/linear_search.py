def search(arr,n,x):
    for i in range(0,n):
        if (arr[i]==x):
            return i
    return -1

arr=[3,5,7,1,9,9]
x=8
n=len(arr)

result = search(arr,n,x)
if(result==-1):
    print("element not present in array")
else:
    print(" element is present at index",result)
