#swap two elements in nArr at postion i and j
def swap(i, j, nArr):
    if i!=j:     
        temp = nArr[j]
        nArr[j] = nArr[i]
        nArr[i] = temp
 
#function to sort elements in the list
def selectionSort(nArr):    
    for i in range(0, len(nArr)):
        small = i
        for j in range(i+1, len(nArr)):
            if nArr[j] < nArr[small]:
                small = j
        swap(i, small, nArr)
 
#list containing elements to sort        
nArr = [34,456, 5, 5,67]
selectionSort(nArr)
print(nArr)