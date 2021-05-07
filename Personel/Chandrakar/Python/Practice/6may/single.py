#single inheritance

class Base:
    def __init__(self):
        self.num=int(input("Enter the number  = "))
class Drive(Base):
    def check(self):
        if self.num%2 ==0:
            print(f"{self.num} is a even number")
        else:
            print(f"{self.num} is a odd number ")

obj = Drive()
obj.check()                        