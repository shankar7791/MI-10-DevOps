def bubbleSort(list1):
    for i in range(len(list1)-1,0,-1):
         for j in range(i):
             if list1[j]>list1[j+1]:
                 temp=list1[j]
                 list1[j]=list1[j+1]
                 list1[j+1]=temp
    return[list1]


def selectionSort(list1):
    for i in range(len(list1)):
        min=i
        for j in range(i,len(list1)):
            if list1[j]<list1[min]:
                min=j
        temp=list1[i]
        list1[i]=list1[min]
        list1[min]=temp
    return [list1]
            


              

list1=[5,10,2,4,8,9]
print(bubbleSort(list1))
print(selectionSort(list1))

