#Multilevel Inheritance

class Parent:
      def func1(self):
          print("I am parent of child 1 ")
class Child1(Parent):
      def func2(self):
          print("I am Parent of child 2")
class Child2(Child1):
      def func3(self) :
          print("I am not Parent now") 
ob = Child2()
ob.func1()
ob.func2()
ob.func3()