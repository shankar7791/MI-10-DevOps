#Single Inheritance

class Student():
   
   def __init__(self, name, enrollment):
      self.name = name
      self.enrollment = enrollment
   def displayB(self):
      print("Name: ",self.name)
      print("Enrollment No.: ",self.enrollment)

class College( Student ):
    def __init__(self, name, enrollment, admnyear, branch):
      self.admnyear = admnyear
      self.branch = branch
      Student.__init__(self, name, enrollment)
    def displayC(self):
        print("Admission Year: ",self.admnyear)
        print("Branch: ",self.branch)

obj = College('Teju',1223345,2021,"CSE")
obj.displayB()
obj.displayC()