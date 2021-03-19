def max():

    arr=[]
    n=int(input("Size of array  "))
    for x in range(0,n):
        a=int(input("Enter the element  "))
        arr.append(a)
    size=len(arr)
    a = arr[0] ; b = arr[1]
    if size<2:
        print("There is no pair of numbers")
    else:
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i] * arr[j] > a*b:
                    a=arr[i] ; b=arr[j]
    print(a,b)
max()


