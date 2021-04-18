
    #Arithmetic operators
    #Assignment operators
    #Comparison operators
    # * Logical operators
    #Identity operators
    #Membership operators
    #Bitwise operators

a=int(input("ENter the first number : "))
b=int(input("Enter the second number : "))
if((a>b) and (b<a)):
    print("a is greater than b")
else:
    print("b is greater than a")
if((a>b)or(a<b)):
    print("a and b are not equal")
else:
    print("a and b are equal")
if not((a>b) and (b<a)):
    print("a is less than b")
else:
    print("b is less than a")