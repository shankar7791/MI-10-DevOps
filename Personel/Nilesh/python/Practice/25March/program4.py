class Class1:
    def m(self):
        print(" Class1") 
        
class Class2(Class1):
    def m(self):
        print(" Class2")
  
class Class3(Class1):
    def m(self):
        print(" Class3")  
         
class Class4(Class2, Class3):
    pass   
      
obj = Class4()
obj.m()