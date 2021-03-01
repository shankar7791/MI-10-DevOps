n = int(input("Enter the number:"))
i = 0
fib=0
n1=1
n2=0
while i<n:
    fib=n1+n2
    n1=n2
    n2=fib
    print(n1)
    i =i+1