import array as arr
def selection():
    a=[]
    n=int(input("Enter the size of array  "))
    for i in range(0,n):
        arr=int(input("Enter the array element  "))
        a.append(arr)
    print(f"Array is  {a}")
    
    for array in range(n):
        for itr in range(array+1,n-1):
    
            if(a[array]>a[itr]):
                
                temp=a[array]
                a[array]=a[itr] 
                a[itr]=temp
                
    print(f"Sorted Array is{a}")
selection()