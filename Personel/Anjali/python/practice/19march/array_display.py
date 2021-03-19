import array as arr
def array():
    a=[]
    n=int(input("Enter the size of array  "))
    for i in range(0,n):
        arr=int(input("Enter the array element  "))
        a.append(arr)
    print(f"Array is  {a}")
array()