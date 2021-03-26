class father():
    def fun1(self):
        return("I'm  the father of child")
class mother(father):
    def fun2(self):
        return("I'M the mother of  child")
class child(mother):
    def fun3(self):
        return("I'M the child")
d=child()
print(d.fun1())
print(d.fun2())
print(d.fun3())