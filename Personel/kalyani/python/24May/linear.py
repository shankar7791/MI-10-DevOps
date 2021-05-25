def linear_search(arr,size):
    for i in range(len(arr)):
       if arr[i]==size:
           print(size," found at index ",i+1)
           break


#driver code
arr=[]
size= int(input(" Enter the size of list :"))
for i in range(size):
    val=int(input(" Enter the number:"))
    arr.append(val)
size=int(input(" Enter the value to search:"))
linear_search(arr,size)3
