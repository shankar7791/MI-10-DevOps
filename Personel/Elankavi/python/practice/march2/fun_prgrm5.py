def fibanocci_series():
    n0,n1=0,1
    a=int(input("Enter how many digits : "))
    print(n0)
    while(a>0):
        n=n0+n1
        print(n)
        n0=n1
        n1=n
        a-=1
fibanocci_series()

