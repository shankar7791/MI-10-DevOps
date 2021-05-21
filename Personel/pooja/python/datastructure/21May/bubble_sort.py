def bubble_sort(array):
    for i in range(len(array)):#acces element
        for j in range(0,len(array)-i - 1): #loop to compare element
            if array[j]>array[j+1]: #compare adjecent element
            #swapping elements
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
data = [-3,9,7,1,5,45,19,6,2]
bubble_sort(data)
print('Sorted Array in Ascending Order:')
print(data)

