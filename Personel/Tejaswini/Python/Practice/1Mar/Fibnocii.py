n=int(input("Enter number:"))
n1=1
n2=0
n3=0

for i in range(0,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n1)