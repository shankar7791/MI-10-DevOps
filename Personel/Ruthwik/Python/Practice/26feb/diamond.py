n=int(input("enter rows"))
r=0

while r<n:
    s=n-r+1
    while s>0:
        print(end=" ")
        s=s-1
    c=r-1
    while c>0:
        print("*", end=" ")
        c=c-1
    r=r+1
    print()

while r>0:
    s=n-r+1
    while s>0:
        print(end=" ")
        s=s-1
    c=r-1
    while c>0:
        print("*", end=" ")
        c=c-1
    r=r-1
    print()
print()