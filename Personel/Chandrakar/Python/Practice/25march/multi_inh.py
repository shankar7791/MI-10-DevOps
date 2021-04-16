#multiple inheritance add two number 
class base:
    def __init__(self):
        self.num = int(input("Enter the 1 st number : "))

class base2:
    def input(self):
        self.num2 = int(input("Enter the 2nd number : "))
class drive(base,base2):
    def add (self):
        super().input()
        self.result=self.num + self.num2
        print(f"{self.num} + {self.num2} = " ,self.result)
ob = drive()    
ob.add()