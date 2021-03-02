def add():
    a = int(input("enter the number :"))
    b = int(input("enter the number :"))
    if (a > 100) and (b < 100):
        c = a + b
        print(a,"+",b,"=",c)
    elif (a < 100) or (b < 100) :
        c = a - b 
        print(c) 
    else :
        print("a and b is equal ")
add()        
          