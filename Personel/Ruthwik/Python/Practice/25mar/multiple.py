# Multiple Inheritance

class Father:
      def func1(self):
          print("I am father of child")
class Uncle:
      def func2(self):
          print("I am Uncle of child")
class Child(Father,Uncle):
      def func3(self):
          print("I am child")
ob = Child()
ob.func1()
ob.func2()
ob.func3() 