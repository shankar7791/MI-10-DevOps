#Python program to print Pascal's Triangle
def fact(f):
    if f < 0:
        return 0
    elif f == 1 or f == 0:
        return 1
    else:
        return f * fact(f-1)

n = int(input('Enter the no of raw you want to print:'))

for i in range(n):
    for j in range(n-i+1):
        print(end=' ') # ---> for left spaces
    for j in range(i+1):
        print(fact(i)//(fact(j)*fact(i-j)), end=' ')
    print()

