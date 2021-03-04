def f(n):
    b=1
    for c in range(1,n+1):
        b = b*c
    
    return b
n = int(input("Enter the number : "))
for i in range(0, n):
    for j in range(1,n-i):
        print("  ", end="")
    for k in range(0, i+1):
        a = int(f(i)/(f(k)*f(i-k)))
        print("  ", a, end="")
    
    print()