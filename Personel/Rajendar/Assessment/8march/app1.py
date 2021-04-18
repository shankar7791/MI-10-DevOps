

# Function to check if binary representation of
# a number is pallindrome or not

def binaryPallindrome(num):

    binary = bin(num)

    binary = binary[2:]

    return binary == binary[-1::-1]


if __name__ == "__main__":
    num = 9
    print(binaryPallindrome(num))
