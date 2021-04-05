#hybrid inheritance

class Parent:
    def func1(self):
        print("I'm from Mumbai")
 
class Child(Parent):
    def func2(self):
        print("I'm from Thane")
 
class Child2(Parent):
    def func3(self):
        print("I'm from Vashi")

class child3(Child ,Parent):
    def func4(self):
        print("I'm from kalyan")
 
ob = child3()
ob.func1()
ob.func2()
ob.func4()