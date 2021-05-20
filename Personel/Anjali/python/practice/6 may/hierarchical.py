class grandparent:
    def gp(self):
        print("grandparent class")

class parent(grandparent):
    def par(self):
        print("from grandparent to parent")

class child(grandparent):
    def chi(self):
        print("from grandparent to child")

obj = parent()
obj1 = child()
obj.gp()
obj.par()
obj1.chi()

