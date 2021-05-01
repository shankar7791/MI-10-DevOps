class student:
    number = 0
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
       
        student.number += 1

obj1= student(12,13)
obj2 = student(14,15)
print(student.number)

