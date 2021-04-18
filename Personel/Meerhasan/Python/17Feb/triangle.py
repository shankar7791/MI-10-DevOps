num1 = float(input("Enter first side : "))
num2 = float(input("Enter seceond side : "))
num3 = float(input("Enter third side : "))           # CALCULATE AREA OF TRIANGLE
s = (num1 + num2 + num3) / 2
area = (s*(s-num1)*(s-num2)*(s-num3)) ** 0.5
print("Area of the Triangle is : %0.2f "%area)

