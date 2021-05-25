def binary_search(arr,size,key):
    i=0
    j=size-1
    flag=0
    while i<j and flag==0:
        mid=(i+j)//2
        if arr[mid]==key:
            pos=mid+1
            flag=1
            if arr[mid]<key:
                i=mid+1
            if arr[mid]>key:
                j=mid-1
    if flag==1:
        print(" Element found at", pos,"position.")
    else:
        print(" Element not found")
        
        
#driver code
arr=[]
size= int(input(" Enter the size of list :"))
for i in range(size):
    val=int(input(" Enter the number:"))
    arr.append(val)
key=int(input(" Enter the value to search:"))
binary_search(arr,size,key)