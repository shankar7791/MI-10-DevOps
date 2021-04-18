#program to find the right angle triangle give two sides 
a = int(input("Enter the one side of triangle : "))
b = int(input("Enter the another side of a triangle : "))
i=a**2
j=b**2
k=i+j
l=k ** 0.5
print("The third side of triangle is : ",l)
