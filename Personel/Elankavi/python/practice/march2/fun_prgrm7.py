def fun():
    b=""
    for row in range(0,6):
        for coloumn in range(0,11):
            if(((row==0 or row ==5) and (coloumn>0 and coloumn<10)) or ((row!=0 and row!=5) and (coloumn == 0 or coloumn == 10))):
                b=b+"*"
            else:
                b=b+" "
        b=b+"\n"
    print(b)
fun()