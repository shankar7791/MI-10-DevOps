
#init method 
class Person:   
    def __init__(self, name,age): 
        self.name = name 
        self.age = age
    def say_hi(self): 
        print("my name is", self.name) 
        print("age is : ",self.age)
a = input("enter the name : ") 
b = int(input("enter the age : "))
p = Person(a,b) 
p.say_hi() 