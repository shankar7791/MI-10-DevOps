#Python program to construct the following pattern, using a nested while loop.

n=5
i=1
while i<n:
    j=1
    while j<=i:
        print("*", end= " ")
        j=j+1
    print("")
    i=i+1

while i>0:
    j=1
    while j<=i:
        print("*", end=" ")
        j=j+1
    print("")
    i=i-1 