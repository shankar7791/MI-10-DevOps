import array as arr
def bubble():
    a=[]
    n=int(input("Enter the size of array  "))
    for i in range(0,n):
        arr=int(input("Enter the array element  "))
        a.append(arr)
    print(f"Array is  {a}")

    for outer in range(n):
        for itr in range (0,n-1):
            
            if (a[itr]>a[itr+1]):
                
                temp=a[itr]
                a[itr]=a[itr+1]
                a[itr+1]=temp
                
    print(f"sorted array is{a}")
bubble()