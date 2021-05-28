def linearsearch(arr,x):
    l=len(arr)
    for i in range(0,l):
       
        if(arr[i]==x):
            return i
    return -1

arr=[1,7,8,5,44,332,67,90]
x=44
r=linearsearch(arr,x)
if(r == -1):
    print("Element not found")
else:
    print("the no found at index",r)

