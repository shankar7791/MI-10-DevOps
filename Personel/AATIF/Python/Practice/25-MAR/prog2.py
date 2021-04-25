#addition in hybrit inheritance
class base:
    def __init__(self):
        self.num = int(input("Enter the 1 st number : "))

class base2(base):
    def input(self):
        self.num2 = int(input("Enter the 2nd number : "))
class base3(base):
    def input2(self):
        self.num3 = int(input("Enter the 3nd number : "))      
class drive(base2,base3):
    def add (self):
        super().input()
        super().input2()
        self.result=self.num + self.num2 + self.num3
        print(f"{self.num} + {self.num2} + {self.num3} = " ,self.result)
ob = drive()    
ob.add() 