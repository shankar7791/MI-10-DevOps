def search(a, b):

    for d in b:

        if a == d:

            m = True

            break

        else:

            m = False

    return m


x = [10, 20, 10, 40, 50, 60, 70]

target = int(input("Enter the number:"))

for i in x:

    if i < target:

        pair = int(target)-int(i)

        in2 = search(pair, x)

        if in2 == True:

            print("the first number= %d the second number %d" % (i, pair))

            break
