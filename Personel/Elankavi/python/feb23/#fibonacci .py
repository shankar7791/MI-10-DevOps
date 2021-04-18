#fibonacci series between 0 to 50
t=50
n1,n2=0,1
i=0
print("Fibonacci Series of 0 to 50 numbers is : ")
while(i<=50):
    print(n1)
    n=n1+n2
    n1=n2
    n2=n
    i=i+1
    
