#Hybrid Inheritance

# Python program to demonstrate
# hybrid inheritance
'''
     |---------- School
     |         |       |
     |     student1  student2
     |       |
student3------
'''

class School:
	def func1(self):
		print("School name is DVMK")

class Student1(School):
	def func2(self):
		print("Student1 is studying in school DVMK")

class Student2(School):
	def func3(self):
		print("Student2 is studying in school DVMK")

class Student3(Student1, School):
	def func4(self):
		print("Student 3 is studying in school DVMK also his guide is student1")


object = Student3()
object.func1()
object.func2()
object.func4()