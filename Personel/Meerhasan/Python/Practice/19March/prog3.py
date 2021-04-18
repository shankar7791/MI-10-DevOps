



import array as a

val = a.array("i", [78,65,94,63,70,3,72,67,12,45])

print(*val)
n = int(input("Please Index You Wnat To delete => "))

del val[n]

print(*val)
    