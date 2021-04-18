r = int(input("Enter the number of rows : "))
for i in range(0, r):
    c= 1

    for j in range(1, r-i):
        print("  ", end="")
    
    for k in range(0, i+1):
        print("  ", c, end="")
        c = int(c * (i - k) / (k + 1))

    print()