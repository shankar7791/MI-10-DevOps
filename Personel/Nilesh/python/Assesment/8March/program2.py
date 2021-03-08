def palindrome(n):
    binary = bin(n)
    binary = binary[2:]
    if binary == binary[-1::-1]:
        print(n,"is palindrome")
    else:
        print(n,"is not palindrome")

n = int(input("enter the number : "))
palindrome(n)