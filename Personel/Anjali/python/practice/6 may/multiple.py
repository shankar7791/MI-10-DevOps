class grandparent:
    def gp_fun(self):
        print("This is grandparent class")

class parent:
    def p_fun(self):
        print("This is parent class")

class child(grandparent,parent):
    def c_fun(self):
        print("This is child class")

obj = child ()
obj.gp_fun()
obj.p_fun()
obj.c_fun()