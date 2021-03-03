

def math():

    import math

    w = float(input("Enter the Width of a Right Angled Triangle: "))
    h = float(input("Enter the Height of a Right Angled Triangle: "))

    Area = 0.5 * w * h

    c = math.sqrt((w*w) + (h*h))
    P = w + h + c

    print("\nArea of a right angled triangle is: %.2f" %Area)
    print("Other side of right angled triangle is: %.2f" %c)
    print("Perimeter of right angled triangle is: %.2f" %P)

math()
