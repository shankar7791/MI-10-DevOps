# Check whether the triangle is valid or not if angles are given using class
class triangle:

    def __init__(self,a1,a2,a3):

        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    
    num_of_sides = 3

    def check_angles(self):
        my_tri = self.a1 + self.a2 + self.a3
        if my_tri == 180:
            print('It is a valid triangle')
        else:
            print('It is not a valid triangle')
        
    
a=int(input('enter angle 1 : '))
b=int(input('enter angle 2 : '))
c=int(input('enter angle 3 : '))
t=triangle(a,b,c)
print('the number of sides = ',t.num_of_sides)
t.check_angles()