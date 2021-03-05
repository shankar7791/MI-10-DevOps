#program to get the factorial 0f the number :

# Algorithm 
# :Take input from user
# :Assign a function
# :using the condtional statement
#4: if conditional is True execute the statement
# 5: elif conditional is True execute the elif statement and print the value
# 6 : call the function


def factorial():
    factorial=1
    a=int(input("Enter the number : "))
    if(a>0):
        for i in range(1,a+1):
            factorial=factorial*i
        print(f"The factorial of {a} is : ",factorial)
    elif(a==0):
        print(f"The factorial of {a} is 1 ")


factorial()