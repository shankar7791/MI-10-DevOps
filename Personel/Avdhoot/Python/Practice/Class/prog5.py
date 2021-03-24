#A class constructed by a radius 
# and two methods which will compute the area and the perimeter of a circle

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

result = Circle(int(input("Enter the Radius: ")))
print(result.area())
print(result.perimeter())