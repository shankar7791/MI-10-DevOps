#Check if Binary representation is Palindrome or not in Python 

A = int(input("Enter a number : "))
B = int(bin(A)[2:])
reverse=str(B)[::-1]

print("The binary representation of number:", B)

if int(reverse)==B:
    print("True")
    print(f"The binary representation of the {A} is {B} which is palindrome as well")
else : 
    print("False")
    print(f"The binary representation of the {A} is {B} which is not palindrome")
