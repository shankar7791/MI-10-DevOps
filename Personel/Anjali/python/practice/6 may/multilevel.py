class grandparent:
    def gp(self):
        print("grandparent class")

class parent(grandparent):
    def per(self):
        print("from grandparent to parent class")

class child(parent):
    def chi(self):
        print("from parent to child")

obj = child ()
obj.gp()
obj.per()
obj.chi()