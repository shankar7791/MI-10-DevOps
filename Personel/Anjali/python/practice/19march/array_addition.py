import array as arr
def addition():
    a=[]
    add=0
    n=int(input("Enter the size of array"))
    for i in range(0,n):
        arr=int(input("Enter the element"))
        a.append(arr)
        add=add+a[i]
    print(f"Array is  {a}")
    print(f"Addition is  {add}")
addition()