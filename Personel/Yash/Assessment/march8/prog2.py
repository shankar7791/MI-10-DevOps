# Program 2 : Check if Binary representation is Palindrome in Python 

num=int(input("Enter the number : "))

binary=bin(num)
temp_binary = binary[2:]
print("Binary representation of a given number is : ",temp_binary)

print("The reverse of binary represetaion is :",temp_binary[::-1])

if temp_binary==temp_binary[::-1]:
    print("Binary representation is a Palindrome ")
else :
    print("Binary representation is not a Palindrome")