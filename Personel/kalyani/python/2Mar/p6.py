#Fibonacci series


def fib():
    n=int(input("enter range : "))
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0',a,b,end=" ")
        for n in range(n-3):
            sum=a+b
            b=a
            a=sum
            print(sum, end=" ")
        print()
        return b

fib()

