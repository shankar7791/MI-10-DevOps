def Addition(num1,num2):
    result  = num1 + num2
    return result

def substraction(num1,num2):
    result = num1 - num2
    return result

def multiplication(num1,num2):
    result = num1 * num2
    return result

def division(num1,num2):
    result = num1 // num2
    return result

def modulus(num1,num2):
    result = num1 % num2
    return result

def exponent(num1,num2):
    result = num1 ^ num2
    return result

print("***MENU***")
print("1.Addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
print("6.exponent")

while True:

    Choice = input("Enter the choice number(1/2/3/4/5/6) : ")

    if Choice in ('1','2','3','4','5','6'):
        num1 = int(input("Enter the Number : "))
        num2 = int(input("Enter the number : "))

        if Choice == '1':
            print(num1,"+",num2, "=",Addition(num1,num2))

        if Choice == '2':
            print(num1, "-", num2, "=",substraction(num1,num2))

        if Choice == '3':
            print(num1, "*", num2,"=",multiplication(num1,num2))

        if Choice == '4':
            print(num1, "//", num2, "=",division(num1,num2))

        if Choice == '5':
            print(num1, "%", num2, "=",modulus(num1,num2))

        if Choice == '6':
            print(num1, "^", num2, "=",exponent(num1,num2))
        
        
    else:
        print("Invalid choice")




