def insertion(list1):
    for i in range(1,len(list1)):
        value = list1[i]

        j = i-1

        while j>= 0 and value < list1[j]:
            list1[j+1] = list1[j]

            j -= 1
        list1[j+1] = value

    return list1

list1 = []

for i in range(0,5):
    A = int(input())
    list1.append(A)
print(list1)

print("the unsorted list :",list1)

print("the sorted list : ",insertion(list1))