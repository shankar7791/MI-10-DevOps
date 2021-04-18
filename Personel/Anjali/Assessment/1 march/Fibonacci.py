val=int(input("Enter the number"))
first=0
second=1
i=0

while i<val:
    if i<=1 :
        j=i
    else :
        j=first+second
        first=second
        second=j
    print(j)
    i=i+1