# hierarchical inheritance

class details:
    def __init__(self):
        self.__id = "<NO ID>"
        self.__name = "<NO Name>"
        self.__gender = "<NO Gender>"
    
    def setdata(self, id, name, gender):
        self.__id = id
        self.__name = name
        self.__gender = gender

    def showdata(self):
        print("ID : ",self.__id)
        print("NAME : ",self.__name)
        print("gender : ",self.__gender)

class employee(details):
    
    def __init__(self):
        self.__company = "<Company>"
        self.__dept = "<nodept"

    def setemployee(self, id, name, gender, comp, dept):
        self.setdata(id, name, gender)
        self.__company = comp
        self.__dept = dept

    def showemployee(self):
        self.showdata()
        print("company : ",self.__company)
        print("Department :",self.__dept)

class Doctor(details): #Inheritance
    def __init__(self):
        self.__hospital="<No Hospital>"
        self.__dept="<No Dept>"

    def setemployee(self,id,name,gender,hos,dept):
        self.setdata(id,name,gender)
        self.__hospital=hos
        self.__dept=dept

    def showemployee(self):
        self.showdata()
        print("Hospital: ", self.__hospital)
        print("Department: ", self.__dept)

print("Employee Object")
e=employee()
e.setemployee(1,"Prem Sharma","Male","IT","Devloper")
e.showemployee()
print("\nDoctor Object")
d = Doctor()
d.setemployee(1, "pankaj", "male", "aiims", "eyes")
d.showemployee()

