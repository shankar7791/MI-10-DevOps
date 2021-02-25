#comparison operator

x = 10
y = 20

if x == y:
    print("True")
else:
    print("false")

if x != y :
    print("True")
else:
    print("false")

if x < y:
    print("x is less than y ")
    if y > x:
        print("y is greater than x")
    else:
        print("y is less than x")
else:
    print("x is greater than y")

if x <= y:
    print("x is less than or equal to y ")
    if y > x:
        print("y is greater than or equal to x")
    else:
        print("y is less than or equal to x")
else:
    print("x is greater than or equal to y")


