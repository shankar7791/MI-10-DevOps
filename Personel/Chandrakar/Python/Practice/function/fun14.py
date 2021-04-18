def prim_e():
    l = int(input("Enter Strating Range:"))
    h = int(input("Enter Ending Range:"))
    while l <= h:
        f = -1
        j = 2
        while j <= l/2:
            if (l%j) ==0:
                f = f+1
                j = j + 1
            else:
                j = j +1

        if f == -1:
            print(l, end=" ")
            l = l + 1
        else:
            l = l+1
prim_e()  
prim_e()      