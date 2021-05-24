# simple level inheritance

class person:
    def_init_(self,name,age)
    self.name=name
    self.age=age
    def display(self):
        print('Name :', self.name)
        print('Age :', self.age)
        
class student(person):
    def_init_(self,roll no,name,age,per)
        self.roll no = roll no
        self.per=per
    def display(self):
        print('Roll no:',self.roll no)
        print('Per :',self.per)

s1 = student(101 , 'kalyani ',25 ,79.90)
print('Student Details :',end ='')
s1.display ()
    