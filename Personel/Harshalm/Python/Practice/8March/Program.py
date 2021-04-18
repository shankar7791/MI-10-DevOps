#Create a simple calculator

def addition():
    num1 = int(input("Enter the num1 :-"))
    num2 = int(input("Enter the num2 :-"))
    add = num1 + num2
    print("Addition Result :-", add)

def substraction():
    num1 = int(input("Enter the num1 :-"))
    num2 = int(input("Enter the num2 :-"))
    sub = num1 - num2
    print("Substraction Result :-", sub)

def multiplication():
    num1 = int(input("Enter the num1 :-"))
    num2 = int(input("Enter the num2 :-"))
    mul= num1 * num2
    print("Multiplication Result :-", mul)

def division():
    num1 = int(input("Enter the num1 :-"))
    num2 = int(input("Enter the num2 :-"))
    div = num1 / num2
    print("Division Result :-", div)

def modulus():
    num1 = int(input("Enter the num1 :-"))
    num2 = int(input("Enter the num2 :-"))
    mod = num1 % num2
    print("Modulus Result :-", mod)

def exponent():
    num1 = int(input("Enter the num1 :-"))
    num2 = int(input("Enter the num2 :-"))
    expo = num1 ^ num2
    print("Exponent Result :-", expo)

print("**** Basic Calculator ****")
print("Operation Performed :-")
print("1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n 5.Modulus \n 6. Exponent :-")
choice = int(input("Enter your choice :-"))
if choice == 1 :
    addition()
elif choice == 2 :
    substraction()
elif choice == 3 :
    multiplication()
elif choice == 4 :
    division()
elif choice == 5 :
    modulus()
elif choice == 6 :
    exponent()
else :
    print("Enter the invalid choice:-")

    