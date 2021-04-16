#Hierarchical Inheritance

class Parent:
      def func1(self):
          print("I am parent of child 1 and child 2")

class Child1(Parent):
      def func2(self):
          print("I am child 1")

class Child2(Parent):
      def func3(self):
          print("I am child 2")


obj1 = Child1()
obj1.func1()
obj1.func2()

obj2 = Child2()
obj2.func1()
obj2.func3() 
