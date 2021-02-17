a=int(input("Enter value for first side:"))
b=int(input("Enter value for second side:"))
c=int(input("Enter value for third side:"))


sum=(a+b+c)/2

#calculate the area
area = (sum*(sum-a)*(sum-b)*(sum-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
