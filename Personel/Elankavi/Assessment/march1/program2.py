#fibonacci series 
t=int(input("How many digits of Fibonacci Series : "))
n1,n2=0,1
i=0
print(f"Fibonacci Series of 0 to {t} digit is : ")
while(i<=t):
    print(n1)
    n=n1+n2
    n1=n2
    n2=n
    i=i+1
