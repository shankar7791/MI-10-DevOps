from collections import UserDict
class mydict(UserDict):
    def print(self):
        print(self.data)
    def insert(self):
        raise RecursionError("Insertion is not allowed")
    def delete(self):
        raise RecursionError("deletion is not allowed")
d = {
    'a' : 3 , 
    'b' : 4,
    'c' : 5
}
d = mydict(d)
d.print()
d.insert()
d.delete()