# Quick sort program
def partition(arr,low,high):
    i = low -1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
        else:
            pass

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    if low<high:
        spit_point = partition(arr,low,high)

        quick_sort(arr,low,spit_point-1)
        quick_sort(arr,spit_point+1,high)

arr = [10,9,30,20,50,40]        
n = len(arr)
quick_sort(arr,0,n-1)
for x in range(n):
    print("%d" % arr[x],end=" ")
print("\n")    