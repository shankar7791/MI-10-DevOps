


num = int(input("Enter A Number => "))

binary = bin(num)
binary = binary[2:]
rev = binary[::-1]

if rev == binary :
    print(f"True \n \nBinary representation of a {num} is {binary} Which is palindrome as well " )

else :
   print(f"True \n \nBinary representation of a {num} is {binary} Which is not a palindrome " )


