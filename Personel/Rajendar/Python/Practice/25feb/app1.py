n = 1234
s = 0
while True:
    k = str(n)
    if k == k[::-1]:
        print("palindrome")
        break
    else:
        m = int(k[::-1])
        n += m
        s += 1
