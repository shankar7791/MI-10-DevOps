def binary_search(a,start,end):
    while(start<=end):
        mid=(start+end)//2
        if(n==a[mid]):
            return mid
        elif(n<a[mid]):
            end=mid-1
        elif (n>a[mid]):
            start=mid+1
    return -1
l=[16,19,12,19,15,11,17,20,15,14]
n=int(input("choice the search of this array ="))
ind = binary_search(l,0,len(l)-1)

if(ind==1):
    print(" element not found")
else:
    print("element is found",ind)