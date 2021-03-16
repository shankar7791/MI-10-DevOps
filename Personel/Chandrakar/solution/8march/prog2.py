def pail(b):
    r = b[::-1]
    if(b==r):
        print(b==r ,"is palindrome")
    else:
        print(b==r,"not palindrom")
n = int(input("enter the number"))
b = bin(n).replace("0b","")
pail(b)            