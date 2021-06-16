from collections import UserList

class List(UserList):
    def print(self):
        print(self.data)
    def insert(self):
        self.data.append(input("Enter the number to insert : "))
        print("After insert : ",self.data)
    def remove(self):
        self.data.remove(input("Enter the number to remove : "))
        print("After remove : ",self.data)
l = List(list(input("Enter the list : ")))
l.print()
l.insert()
l.remove()