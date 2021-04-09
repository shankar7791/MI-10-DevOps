'''Student Management System.

Create program for Student Management System using OOP Concepts

Problem Statement:
Write a program to build a simple Student Management System using Python which can perform following operations:

Accept
Display
Search
Delete
Update
'''

class Student:

    def __init__(self, name, roll, sr1, sr2):
        self.name = name
        self.roll = roll
        self.sr1 = sr1
        self.sr2 = sr2

    # Function to create and append students
    def accept(self, Name, Roll, score1, score2):
        obj = Student(Name, Roll, score1, score2)
        ls.append(obj)

    # Display student details
    def display(self, obj):
        print("Name   : ", obj.name)
        print("Roll No : ", obj.roll)
        print("Score 1 : ", obj.sr1)
        print("Score 2 : ", obj.sr2)
        print("\n")


ls = []
obj1 = Student('', 0, 0, 0)

print("\nOperations used, ")
print("\n1.Accept Student details\n"
      "2.Display Student Details\n" 
       "3.Search Details of a Student\n"
        "4.Delete Details of Student" 
      "\n5.Update Student Details\n6.Exit")


obj1.accept("A", 1, 100, 100)
obj1.accept("B", 2, 90, 90)
obj1.accept("C", 3, 80, 80)

print("\nList of Students\n")
for i in range(ls.__len__()):
    obj1.display(ls[i])