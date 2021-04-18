#add two string 
class Person:   
    def __init__(self, str1,str2): 
        self.str1 = str1
        self.str2 = str2
    def say_hi(self): 
        return self.str1 + self.str2
a = input("enter the 1st string : ") 
b = input("enter the 2nd string : ")
p = Person(a,b) 
print("after adding two string is : ", p.say_hi())