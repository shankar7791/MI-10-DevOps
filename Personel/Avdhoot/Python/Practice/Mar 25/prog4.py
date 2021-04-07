#hierarchical inheritance

class Parent:
    def func1(self):
        print("This is function 1")

class Child(Parent):
    def func2(self):
        print("This is function 2")

class Child2(Parent):
    def func3(self):
        print("This is function 3")
 
ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()