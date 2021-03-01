#fibonacci series
n = int(input('Enter a no. where up to you want a series:'))
a = 1
b = 1
print(a)
print(b)
while True:
    c = a + b
    if c > n:
        break
    print(c)
    a = b
    b = c