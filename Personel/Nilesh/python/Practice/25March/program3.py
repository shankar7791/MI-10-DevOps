#multilevel inheritance

class First:
    def input(self):
        self.a = int(input("Enter first number:"))
        self.b = int(input("Enter second number:"))


class Second(First):
    def add(self):
        self.z = self.a + self.b


class Third(Second):
    def result(self):
        print("Sum of two numbers:", self.z)


obj = Third()
obj.input()
obj.add()
obj.result()
