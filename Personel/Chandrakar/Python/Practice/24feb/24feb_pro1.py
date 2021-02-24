#arthmetic oprater
a = int(input("enter the number : "))
b = int (input("enter the 2nd number :"))
if a > b :
    c = a + b
    d = a * b
    print(a,"+",b,"=",c)
    print(a,"*",b,"=,",d)
elif b > a :
    c = b - a
    d = b/a
    print(a,"-",b,"=",c)
    print(a,"/",b,"=,",d)  
else :
    print("both are equal" )
