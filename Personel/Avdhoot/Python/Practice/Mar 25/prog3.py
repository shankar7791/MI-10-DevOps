#multiple inheritance
class Parent1:  
    def sum(self,a,b):  
        return a+b;  
class Parent2:  
    def mul(self,a,b):  
        return a*b;  
class Derived(Parent1,Parent2):  
    def fdiv(self,a,b):  
        return a//b;  
d = Derived()  
print(d.sum(10,20))  
print(d.mul(0.5,8.4))  
print(d.fdiv(30,13))  