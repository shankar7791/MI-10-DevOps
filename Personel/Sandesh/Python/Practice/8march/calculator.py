# Define our function
def calculate():
    operator = input("""
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for exponent
% for modulus

""")

    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))

    if operator == '+':
        num3=num1+num2
        print(num3)

    elif operator == '-':
        num3=num1-num2
        print(num3)

    elif operator == '*':
        num3=num1*num2
        print(num3)

    elif operator == '/':
        num3=num1/num2
        print(num3)
    
    elif operator == "%":
        num3=num1%num2
        print(num3)
    
    elif operator == "**":
        num3=num1**num2
        print(num3)

    else:
        print('You have not typed a valid operator, please run the program again.')

# Call calculate() outside of the function
calculate()