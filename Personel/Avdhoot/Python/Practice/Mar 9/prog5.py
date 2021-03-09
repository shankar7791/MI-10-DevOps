#reverse a string if it's length is 4
def str(str1):
    if len(str1) % 4 == 0:
        str1 = str1[::-1]
    return str1

print(str('xyzs'))
print(str('python'))