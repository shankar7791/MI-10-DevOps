#find area of rectangle
class Rect():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

result = Rect(12,17)
print(result.area())