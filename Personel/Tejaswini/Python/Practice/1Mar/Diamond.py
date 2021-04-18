n =  int(input("Enter no. of rows: "))
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


#for i in range(n):
    #print("1"*(n-i), "*"*(i*2+1))
#for i in range(n-2, -1, -1):
 #   print(" "*(n-i), "*"*(i*2+1))