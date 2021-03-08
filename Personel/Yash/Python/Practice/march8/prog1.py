# Create a simple calculator in python.
# Take choice from user...
# Create menu wise choices
# 1. Addition
# 2. Substraction
# 3. Modulus
# 4. Division
# 5. Multiplication
# 6. Exponent

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def mod(x,y) :
    return x % y
def divide(x, y):
    return x / y
def multiply(x, y):
    return x * y
def exponent(x,y):
    return x ** y



print("Select the Menu choice : ")
print("1.Addition")
print("2.Subtraction")
print("3.Modulus")
print("4.Division")
print("5.Multiplication")
print("6.Exponent")


while True:
    choice = input("Enter the choice(1/2/3/4/5/6): ")
    if choice in ('1', '2', '3', '4', '5','6'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "%", num2, "=", mod(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '6':
            print(num1, "**", num2, "=", exponent(num1, num2))
        break
    else:
        print("Invalid Input")