#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

class Rectangle() :
    def __init__(self) :
        self.length = int(input("Enter Lenth => "))
        self.width  = int(input("Enter Width => "))

    def rectangle_area(self):
        return self.length*self.width

obj = Rectangle()
print("Area Of A Rectangle => ",obj.rectangle_area())