class num():
    def add(self,a,b):
        return("Addition",a+b)
class num2(num):
    def sub(self,a,b):
        return("subtraction",a-b)
d=num2()
print(d.add(6,7))
print(d.sub(6,7))