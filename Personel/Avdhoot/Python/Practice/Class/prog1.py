class Student: 
    def __init__(self, Id, name, cname):
        self.Id = Id
        self.name = name
        self.cname = cname 
student = Student('V12', 'Frank Gibson', 'V')
print(student.__dict__)