#single inheritance check the number even or odd number 
class base:
    def __init__(self):
        self.num=int(input("enter the number : "))
class drive(base) :
    def check(self):
        if self.num%2 == 0:
            print(f"{self.num} is even number")
        else:
            print(f"{self.num} is odd number")            
ob = drive()
ob.check()   