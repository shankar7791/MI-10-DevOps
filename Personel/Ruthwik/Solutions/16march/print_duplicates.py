# Program to print duplicates from a list of integers 

def dupli(list):
    l1=[]

    for i in list:
        if i not in l1:
            l1.append(i)
        else:
            print('The duplicates are : ',i,end=' ')

l=[]
n = int(input("Enter the number of elements in list:"))
for x in range(0, n):
    element = input("Enter element:")
    l.append(element)

print('The entered list is : ', l)

dupli(l)