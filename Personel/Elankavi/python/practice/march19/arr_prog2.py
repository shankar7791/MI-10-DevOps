import array
a=list(input("Enter the number : "))
def array(a):
    while True:


        b=input("""
        1.add the number 
        2.remove
        3.reverse
        4.sort
        5.pop
        6.display
        7.exit

        Enter your choice : """)
        if(b=='1'):
            c=input("Enter the number to add : ")
            (a.append(c))
        elif(b=='2'):
            c=input("Enter the number to remove ")
            (a.remove(c))
        elif(b=='3'):
            
            a.reverse()
        elif(b=='4'):
            a.sort()
        elif(b=='5'):
            c=int(input("enter the number to pop :"))
            (a.pop(c))
        elif(b=='6'):
            print(a)
        elif(b=='7'):
            exit()
        else:
            print("Enter the valid choice")
        print(a)

        
  
array(a)