# multiple inheritance 

class calculation1:
    def sum( self ,a ,b):
        return  a+b
 
# base class 2   
class calculation2:
    def multiplication(self , a ,b):
        return a*b

# Derived class
class Derived ( calculation1 , calculation2):
    def Divide(self, a,b):
        return a/b

# creating constructor
d = derived()
print(d.sum(20,20))
print(d.Multiplication(10,20))
print(d.divide(10,20))
    