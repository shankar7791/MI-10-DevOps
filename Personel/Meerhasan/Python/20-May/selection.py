def selectionSort(array, size):
   
    for step in range(size):
        min = step

        for i in range(step + 1, size):

            if array[i] < array[min]:
                min_idx = i
         
        (array[step], array[min]) = (array[min], array[step])


data = [23, 45, 2, 11, 8, 12]
size = len(data)
selectionSort(data, size)
print('Sorted Using Selection Sort :')
print(data)