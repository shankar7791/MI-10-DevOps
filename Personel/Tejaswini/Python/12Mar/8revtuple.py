#Print Reverse tuple

def reverse(t):
    t1 = t[::-1]
    return t1

t = tuple(input("Enter input : "))
print("Orignal Tuple : ",t)
print("Reverse Tuple : ",reverse(t))