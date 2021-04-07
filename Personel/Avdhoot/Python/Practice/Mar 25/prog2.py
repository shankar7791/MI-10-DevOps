#multi-level inheritance

class Parent:
    def fun1(self):
        print("I am Student of 10th std ")
class Child1(Parent):
    def fun2(self):
        print("I am Student of 9th std")
class Child2(Child1):
    def fun3(self) :
        print("I am not student") 
ob = Child2()
ob.fun1()
ob.fun2()
ob.fun3() 