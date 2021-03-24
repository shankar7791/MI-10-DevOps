#inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print("Person's Name is : ",self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Yash", "Malavade")
x.printname()