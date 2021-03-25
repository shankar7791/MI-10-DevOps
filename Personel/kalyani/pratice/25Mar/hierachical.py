# hierachical inheritance

class school:
    def func1(self):
        self.var1=int(input(" Enter your school name:"))
        print(self.var1)
        
class studentname(school):
    def func2(self):
        self.var2=int(input(" Enter your name:"))
        print(self.var2)
        
class studentage(school):
    def func3(self):
        self.var3=int(input(" Enter your age :"))
        print(self.var3)
    
object1.func2()
object1=studentage()
object1=studentname()
object1.func1()
object.func3()