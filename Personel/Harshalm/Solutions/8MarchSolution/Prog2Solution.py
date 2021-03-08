#binary reprentation is palindrome 


def binaryPalindrome(num):
    
    binary = bin(num)

    binary = binary[2:]

    print('binary of ',num,' is ',binary)

    if binary == binary[-1 :: -1]:
        print(True)
    else:
        print(False)

num=int(input("enter a number : "))
binaryPalindrome(num) 
