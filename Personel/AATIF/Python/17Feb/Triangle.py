a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

s =float((a + b + c) / 2)       # calculate the semi-perimeter

# calculate the area
area = float((s*(s-a)*(s-b)*(s-c)) ** 0.5)
print("The area of the triangle is %0.2f" %area)