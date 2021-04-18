#format string
def format():
    a=int(input("Enter your age : "))
    b=input("Enter your name : ")
    c="your name is {} and age is {}"
    print(c.format(b,a))
format()