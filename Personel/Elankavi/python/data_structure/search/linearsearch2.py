def linearsearch(arr,n):
    left=0
    l=len(arr)
    right=l-1
    p=-1
    for left in range(0,right,1):
        if(arr[left]==n):
            p=left
            print(f"Element found in A {p +1} Position with {left + 1} Attempt")
            break
        if(arr[right]==n):
            p=right
            print(f"Element found in  {p + 1}  Position with {right + 1} Attempt")
            break
        right-=1
        left+=1
        if (p == -1):
            print(f"Not found in Array with {left} Attempt")

arr=[22,44,55,0,98]
n=98
linearsearch(arr,n)