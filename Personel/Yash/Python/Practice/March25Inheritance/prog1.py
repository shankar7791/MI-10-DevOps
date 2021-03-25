# Single Inheritance

class Car :
    def carFun(self) :
        print("Cars have different feature")

class Audi(Car) :
    def audiFun(self) :
        print("Audi has unique design")

obj = Audi()
obj.carFun()
obj.audiFun()