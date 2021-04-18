print("***Performing Assignment Operators***")
print("1.Assigns the value ")
print("2.+= Operater")
print("3.-= operater")
print("4.*= operater")
print("5.%= operater")
print("6.**= operater")
print("7.//== Operater")
selection=int(input("Enter a Selecion"))
if(selection==1):
    print("You Select Assigns the value")
    a=int(input("Enter a First Number: "))
    print("Assign: ",a)
elif(selection==2):
    print("You Select += Operater")
    a=int(input("Enter a First Number: "))
    b=int(input("Enter abSecond Number: "))
    a+=b
    print("+= Operater: ",a)
elif(selection==3):
    print("You Select -= operater")
    a=int(input("Enter a First Number: "))
    b=int(input("Enter b Second Number: "))
    a-=b
    print("-= operater",a)
elif(selection==4):
    print("You Select *= operater")
    a=int(input("Enter a First Number: "))
    b=int(input("Enter b Second Number: "))
    a*=b
    print("*= operater: ",a)
elif(selection==5):
    print("You Select %= operater")
    a=int(input("Enter a First Number: "))
    b=int(input("Enter b Second Number: "))
    a%=b
    print("%= operater: ",a)
elif(selection==6):
    print("You Select **= operater")
    a=int(input("Enter a First Number: "))
    b=int(input("Enter b Second Number: "))
    a**=b
    print("**= operater: ",a)
elif(selection==7):
    print("You Select //== Operater")
    a=int(input("Enter a First Number: "))
    b=int(input("Enter b Second Number: "))
    a//=b
    print("//== Operater: ",a)
    

