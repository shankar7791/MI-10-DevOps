print("***Membership Operators***")
print("1.is Operater")
print("2.is not  Operater |")
selection=int(input("selection.."))

if(selection==1):
    print("your selection is Operator")
    print("Returns true if both variables are the same object")
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x
    print(x is z)
elif(selection==2):
    print("your selection is not  operater")
    a=int(input("Returns true if both variables are not the same object "))
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x
    print(x is not z)
