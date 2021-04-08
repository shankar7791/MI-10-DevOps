#check even odd and + ve -ve
class base:
    def __init__(self):
        self.num = int(input("enter the number : "))

class derive1(base):
    def check(self):
        if self.num % 2 == 0:
            print("Given number is even. ",self.num)
        else :
            print("Given number is odd. ",self.num)

class derive2(base):
    def check(self):
        if self.num > 0:
            print("Given number is +Ve ",self.num)
        else :
            print("Given number is -Ve ",self.num)

ob1 = derive1()
ob1.check()
ob2 = derive2()       
ob2.check() 