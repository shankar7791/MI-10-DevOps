def bubble(list1):

    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j] > list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

list1 = []
for i in range(0,5):
    A = int(input())
    list1.append(A)
print(list1)
print("unsorted list is : ",list1)

print("the sorted list:",bubble(list1))