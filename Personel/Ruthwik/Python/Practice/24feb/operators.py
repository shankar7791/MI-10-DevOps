#Operators

a= float(input("enter a number a:"))
b=float(input("enter a number b:"))
c=float(input("enter a number c:"))
d=float(input("enter a number d:"))
e = 'Hello world'
f = {1:'a',2:'b'}
p=0
q=1
a1=0
x=True
y=False
x1=5.0
y1=5.0
x2="hello"
y2="hello"

print("\n Arithmetic operators")

print("addition :",a+b)
print("Subtraction :",a-b)
print("multiplication :",a*b)
print("division :",a/b)
print("Modulus :",a%b)
print("eaponentiation :",a**b)
print("Floor division :",a//b)

print("\n assignment operators")

print("c =",c)
c+=d
print("c+=d", c)
c-=d
print("c-=d",c)
c*=d
print("c*=d", c)
c/=d
print("c/=d",c)
c%=d
print("c%=d",c)
c//=d
print("c//=d",c)
c**=d
print("c**=d",c)
p&=q
print("p&=q",p)
p|=q
print("p|=q",p)
p^=q
print("p^=q",p)
p>>=q
print("p>>=q",p)
p<<=q
print("p<<=q",p)

print("\n Comparison operators")

print('a > b is',a>b)
print('a < b is',a<b)
print('a == b is',a==b)
print('a != b is',a!=b)
print('a >= b is',a>=b)
print('a <= b is',a<=b)

print("\n Logical operators")

print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

print("\n Identity operators")

print(x1 is not y1)
print(x2 is y2)

print("\n Membership Operators")

print('H' in e)
print('hello' not in e)
print(1 in f)
print('a' in f)

print("\n Bitwise operators")

a1=p&q
print("p&q =",a1)
a1=p|q
print("p|q =",a1)
a1=p^q
print("p^q =",a1)
a1=-p
print("-p =",a1)
a1=p<<2
print("p<<2 =",a1)
a1=p>>2
print("p>>2 =",a1)