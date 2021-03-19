#decending program


list = []  
n = int(input("Enter the number of element :-"))
for i in range(1, n + 1) :
    value = int(input("Enter the value of  %d element :- " %i))
    list.append(value)

for i in range(n) :
    for j in range(i + 1 , n) :
        if list[i] < list[j] :
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print("Element in Descending order :-", list)


import array as arr
def descending():
    l=[]
    temp=0
    n=int(input("Enter the size of array "))
    for i in range(n):
        arr=int(input("Enter the size of array  "))
        l.append(arr)
    print(f"Array is  {l}")
    for x in range(0,len(l)):
        for y in range(x+1,len(l)):
            if(l[x]<l[y]):
                temp=l[x]
                l[x]=l[y]
                l[y]=temp
    print()
    print("Array sorted in descending order: ");    
    for i in range(0, len(l)):    
        print(l[i], end=" ");    
descending()