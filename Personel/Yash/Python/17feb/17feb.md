var1 = 10
var2 = 20
var3 = "yash24"
var4 = True
var5 = False
Var6 = None

sum=var1+var2
print("\n",sum)
print("\n",var1+var2)
print("\t",var1,"\t",var2)
#Identation is very imp 
#(){} not needed
def add():
    a=50
    b=70
    product=a*b
    print("Product is",product)

add()

#print(len(var1)) object of type 'int' has no len()

print("length of string is",len(var3))

print("""
4.Xanthrons
    4.1 Tejaswini
    4.2 Rajkumar
    4.3 Rutwik
    4.4 Yash
""")
#List is the collection of diff datatypes

a=[10,"yash",78.58]
print(a)
print(a[1])

#Tuple
t=(1,2,3,4,5)
print(t,"\nLength of tuple",len(t))

red=(255,0,0)
r,g,b=red
print(r,g,b)

#Dictionary
#Name value or keyvalue
person={"name" :"Yash","Address": "Khed","id":20120}
print(person)
print(person["name"],person["id"])

#set
s={99,1,5,1,5,6,78,45,12,99,78,29}
print(s)

#Boolean
b=0
# true=1 false=0
if b==True:
	print("I am yash")
elif b==False:
	print("I am human")
else:	
	print("Alien")

#addition program
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
sum=num1+num2
print("Addition is " ,sum)

a1=1000
a2="200"

print("Addition is ",a1+int(a2))
print(str(a1)+a2)

