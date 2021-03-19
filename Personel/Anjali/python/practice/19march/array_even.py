import array as arr
def even():
    a=[]
    n=int(input("Enter the size of array  "))
    for i in range(0,n):
        arr=int(input("Enter the element  "))
        a.append(arr)
    print(f"Array is {a}")
    for j in range(n):
        if (a[j]%2==0):
            print(a[j],end=" ")
           
even()