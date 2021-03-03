def swap():
    x = int(input("Enter the Value Of x: "))
    y = int(input("Enter the Value Of y: "))

    temp = x
    x = y
    y = temp

    print("Swapped value of x: ", x)
    print("Swapped value of y: ", y)

swap()
