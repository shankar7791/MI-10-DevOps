class class1 :
    def square(self) :
        self.num = int(input("Enter a number => "))
        self.sq = self.num ** 2
        print("\nSquare root => ",self.sq)

        return self.sq 


class class2(class1) :
    def addition(self) :
        self.n1 = int(input("Enter First Number => "))
        self.n2 = int(input("Enter Second Nmuber => "))

        self.add = self.n1 + self.n2
        print("\nSum => ", self.add)
        return self.add

ob = class2()
while True :
    print("""*\n********* Welcome *********
1. Square Root
2. Addition 
3. Exit 
""" )
# ***********************************************************************************************************************************************************

    ch = int(input("Enter Your Choice => "))

    if ch == 1 :
        ob.square()

    elif ch == 2 :
        ob.addition()

    elif ch == 3 :
        exit()

    else :
        print("\nEnter A Valid Input !!!!")

