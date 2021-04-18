def check_Palin(x):
    rev = x[::-1]
    if (x==rev):
        print("Number is Palindrome.")
    else:
        print("Number is not palindrome.")
n = int(input("Enter the number: "))
x = bin(n).replace("ob","")
check_Palin(x)