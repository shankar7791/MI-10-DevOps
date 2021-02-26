n=int(input("Enter a number"))
while True:
    n1=str(n)
    rev= n1[::-1]
    if n1== rev:
        print(n ,"is palindrome")
        break
    n = int(n1)+int(rev)
    print(f"{n1}+{rev}={n}")