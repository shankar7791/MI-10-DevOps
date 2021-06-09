import array as arr
def insertion():
    a=[]
    n=int(input("Enter the size of array  "))
    for x in range(0,n):
        arr=int(input("Enter the array element  "))
        a.append(arr)
    print(f"Array is  {a}")
    for i in range(1,len(a)):
        empty=a[i]
        hole=i-1
        
        while hole>=0 and empty < a[hole]:
            a[hole+1]=a[hole]
            hole-=1
        a[hole+1]=empty
    print(f"Sorted Array is {a}")
insertion()    
