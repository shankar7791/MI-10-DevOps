# program to add the two numbers without using +
a =int(input("Enter the first number  : "))
b = int(input("Enter the secnd number : "))
while(b != 0):
    c=a & b
    a=a^b
    b=c<<1
print("The sum of two number is : ",a)