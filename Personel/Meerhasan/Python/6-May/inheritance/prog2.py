
# Multi-Level inheritance 

class class1 :
    def square(self) :
        self.num = int(input("Enter a number => "))
        self.sq = self.num ** 2
        print("\nSquare root => ",self.sq)

        return self.sq 
# ************************ Sub Class Of Class1 *************************************************************************************************************

class class2(class1) :
    def addition(self) :
        self.n1 = int(input("Enter First Number => "))
        self.n2 = int(input("Enter Second Nmuber => "))

        self.add = self.n1 + self.n2
        print("\nSum => ", self.add)
        return self.add 

# ************************ Sub Class Of Class2 *************************************************************************************************************

class class3(class2) :
    def sub(self) :
        self.n1 = int(input("Enter First Number => "))
        self.n2 = int(input("Enter Second Nmuber => "))

        self.subs = self.n1 - self.n2
        print("\nSubstraction => ", self.subs)
        return self.subs
    

# ***********************************************************************************************************************************************************

ob = class3()
while True :
    print("""*\n********* Welcome *********

1. Square Root
2. Addition 
3. Substraction
4. Exit 

""" )
# ***********************************************************************************************************************************************************

    ch = int(input("Enter Your Choice => "))

    if ch == 1 :
        ob.square()

    elif ch == 2 :
        ob.addition()

    elif ch == 3 :
        ob.sub()

    elif ch == 4 :
        exit()

    else :
        print("\nEnter A Valid Input !!!!")




