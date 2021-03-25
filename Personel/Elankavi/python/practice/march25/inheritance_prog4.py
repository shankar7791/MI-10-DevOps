class parent1():
    def fun1(self):
        return("I'M the parent1 function")
class parent2():
    def fun2(self):
        return("i'M the parent2 function ")
class child(parent1,parent2):
    def fun3(self):
        return("I'M the child function")
d=child()
print(d.fun1())
print(d.fun2())
print(d.fun3())