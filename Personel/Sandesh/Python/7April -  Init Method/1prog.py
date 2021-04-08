#How to count number of instances of a class in Python?

class Employee:
    number_of_Employee = 0
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary 
        Employee.number_of_Employee += 1

Sandesh= Employee("Sandesh", 22, "40000/-")
Patekar = Employee("Patekar", 22, "50000/-")

print("The number of Employees in the class : " + str(Employee.number_of_Employee))


