class meta(type):
    def __new__(self,class_name,bases,attrs):
        print(attrs)
        return type(class_name , bases,attrs) 
class Dog(metaclass=meta):
    x = 10
    y = 13
    def hello(self):
        print("hi")       