
# binary representation
x = int(input('Enter a number: '))
y = int(bin(x)[2:])

out = str(y)[::-1]
print("The binary representation of number:", y)
if int(out) == y:
    print("The binary representation of the number is a palindrome.")
else:
    print("The binary representation of the number is not a palindrome.")
