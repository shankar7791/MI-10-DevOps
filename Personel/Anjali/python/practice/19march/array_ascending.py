import array as arr
def ascending():
    a=[]
    temp=0
    n=int(input("Enter the size of array "))
    for i in range(n):
        arr=int(input("Enter the size of array  "))
        a.append(arr)
    print(f"Array is  {a}")
    for x in range(0,len(a)):
        for y in range(x+1,len(a)):
            if(a[x]>a[y]):
                temp=a[x]
                a[x]=a[y]
                a[y]=temp
    print()
    print("Array sorted in ascending order: ");    
    for i in range(0, len(a)):    
        print(a[i], end=" ");    
ascending()