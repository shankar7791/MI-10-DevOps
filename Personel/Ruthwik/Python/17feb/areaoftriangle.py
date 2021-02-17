#Calculate area of triangle

a = int(input('Enter first side: '))  
b = int(input('Enter second side: '))  
c = int(input('Enter third side: '))  

# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  

print('The area of triangle is :', area)