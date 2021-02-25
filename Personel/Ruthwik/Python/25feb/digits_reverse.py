#Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure.

n=int(input("Enter a number : "))

while True:
    n1=str(n)
    rev= n1[::-1]
    if n1== rev:
        print(n ,"is palindrome")
        break
    n = int(n1)+int(rev)
    print(f"{n1}+{rev}={n}")