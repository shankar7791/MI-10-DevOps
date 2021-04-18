def kite(n):
    k = n
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i +1):
            print("* ", end="")
        print("")    

    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ",end="")
        print("")
    k=n
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i +1):
            print("* ", end="")
        print("") 

n=int(input("Enter the value for n: "))
kite(n)