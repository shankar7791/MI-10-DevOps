arr=[1,9,6,77,44,5,65,2,4,78]
print("Given array : ")
for i in range(len(arr)):
    print(arr[i],end=" ")
print()

def bubblesort(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(l-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
bubblesort(arr)
print("sorted array : ")
for i in range(len(arr)):
    print(arr[i],end=" ")
print()