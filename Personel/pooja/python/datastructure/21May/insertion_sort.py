def insertionSort(array):
    for step in range (1,len(array)):
        key = array[step]
        j=step-1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j+1]= key
data =[9,2,3,8,1,5]
insertionSort(data)
print("sorted array im ascending order")
print(data)