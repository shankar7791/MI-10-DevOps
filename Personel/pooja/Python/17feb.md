In todays session we have seen Datatypes in pythonas:
A) Programs
1. python program to Add two numbers

num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
sum  = num1 + num2
print("Addition =", sum)56

2. python program to find square root of numbers

number = int (input("enter a number: " ))
sqrt = number ** 0.5
print("square root :", sqrt)

3. python program to calculate area of triangle

a = 5
b = 6
c = 7

s = (a + b + c) / 2
area = (s*(s-a) * (s-b) * (s-c)) ** 0.5

print (" area of the triangle is %0.2f" %area)

4. python program to to swap two variables

x = 5
y = 10

temp = x
x = y
y = temp

print("the value of x after swapping: {}".format(x))
print("the value of y after swapping: {}".format(y))

5. python program to generate random number

import random
print(random.randint(0,9))

6. python program to Convert Celcious to Farenheight

celcius = float(input ("Enter temperature in celcius :"))

fahrenheit = (celcius * 9/5) + 32
print('%0.2f celcius is :%0.2f degree fahrenheit' %(celcius,fahrenheit))


B) Datatypes inpython

1.int
var = 10
print(var)

2.float
var = 22.3
print(var)

3.string
var = "Ambersoft"
print(len(var))

4.list
a = [1,"pooja",3.5,4578]
print(a[1])

5.tuple
t = (2,3)
print(t , "\n" , len(t))
	OR
yellow = (255, 255, 0)
r, g, b = yellow
print (r, g,b ))


6.set
a = {1,2,9,6,3,1,2,9}
print(a)

7.dictionary
person = { "name":"pooja","email":"pooja@gmail.com","age":25}
print(person["name"])

8.boolean
true = 10
a = 10
if b == True:
print("pooja")
else:
print("not pooja")
