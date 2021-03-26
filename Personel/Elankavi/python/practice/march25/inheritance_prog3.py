class parent():
    def fun1(self):
        return("I'M the parent class")
class child1(parent):
    def fun2(self):
        return("I'M the child1 class")
class child2(parent):
    def fun3(self):
        return("I'M the child2 class")
d=child1()
f=child2()
print(d.fun1())
print(d.fun2())
print(f.fun3())
print(f.fun1())