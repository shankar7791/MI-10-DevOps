def fun():
    i=int(input("HOw many names : "))
    while(i>0):
        a=input("Enter the name : ")
        b=input("Enter male or female : ")
        if(b=='m') or (b=='male'):
            print("hello , Mr.",a)
        elif(b=='f') or (b=='female'):
            print("hello , ms.",a)
        else:
            print("Enter the valid input : ")
            i+=1
        i-=1
fun()
fun()
