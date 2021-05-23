#multiple inheritance add three number


class Base:
    def __init__(self):
        self.num=int(input("Enter the number  = "))
class Base1:
    def input(self):
        self.num1=int(input("Enter the number  = "))   
class Base2:
    def input1(self):
        self.num2=int(input("Enter the number  = "))   

class Drive(Base,Base1,Base2):
    def print_d(self):
        super().input()
        super().input1()
        return self.num+self.num1+self.num2

obj = Drive()
print(obj.print_d())                        