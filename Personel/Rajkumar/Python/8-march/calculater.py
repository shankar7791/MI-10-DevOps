#  adds two numbers
def add(x, y):
    return x + y

# subtracts two numbers
def sub(x, y):
    return x - y

#  multiplies two numbers
def mul(x, y):
    return x * y

#  divides two numbers
def div(x, y):
    return x / y

#   modulus two numbers
def mod(x,y):
    return x % y

#   exponrnt two numbers
def exp(x,y):
    return x ** y



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
print("6.Exponent")

while True:
    # Take input from  user
    ch= input("Enter choice: ")

    # Check if choice is one of the four options
    if ch in ('1', '2', '3', '4' , '5' , '6'):
        n1 = float(input("Enter 1st number: "))
        n2 = float(input("Enter 2nd number: "))

        if ch == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif ch == '2':
            print(n1, "-", n2, "=", sub(n1, n2))

        elif ch == '3':
            print(n1, "*", n2, "=", mul(n1, n2))

        elif ch == '4':
            print(n1, "/", n2, "=", div(n1, n2))
        
        elif ch == '5':
            print(n1, "%", n2, "=", mod(n1, n2))

        elif ch == '6':
            print(n1, "**", n2, "=", exp(n1, n2))
        break
    else:
        print("Invalid Input")