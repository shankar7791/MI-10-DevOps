def binary(num):

    binary_con = bin(num)

    binary_con = binary_con[2:]

    print(f"{num} is {binary_con}")

    if binary_con == binary_con[-1 :: -1]:
        print(True)
    else:
        print(False)

n=int(input("enter a number : "))
binary(n) 