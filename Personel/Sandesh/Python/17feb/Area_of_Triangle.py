#calculate area of Triangle

a = float(input("Enter first side : "))
b = float(input("Enter second side : "))
c = float(input("Enter third side : "))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the Triangle is %0.2f" %area)