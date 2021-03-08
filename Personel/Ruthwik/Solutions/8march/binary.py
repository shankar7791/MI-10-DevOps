def binary_rep(num):

    binary_conversion = bin(num)

    binary_conversion = binary_conversion[2:]

    print('binary of ',num,' is ',binary_conversion)

    if binary_conversion == binary_conversion[-1 :: -1]:
        print(True)
    else:
        print(False)

n=int(input("enter a number : "))
binary_rep(n)