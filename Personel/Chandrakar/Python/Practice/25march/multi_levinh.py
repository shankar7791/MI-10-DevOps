#using multilevel inheritance factorial number
class base:
    def __init__(self):
        self.num = int(input("enter the number : "))
        self.fac = 1
class drive(base):
    def fact(self):
        for i in range(1,self.num + 1):
            self.fac=self.fac*i
class child(drive):
    def printm(self):
        return "fectorial is " ,self.fac
ob = child()
ob.fact()
print(ob.printm())
