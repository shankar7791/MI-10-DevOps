# hybrid inheritance

class school:
    def func1(self):
        print(" infant jesus english school :")
        
class student1(school):
    def func2(self):
        print(" my name is koki :")
        
class student2(school):
    def func3(self):
        print(" my name is kalyani :")
        
class student3(school):
    def func4(self):
        print(" my name is sayali :")
        
# driven code
object=student3()
object.func1()
object.func2()
object.func3()
object.func4()