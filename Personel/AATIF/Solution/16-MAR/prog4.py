# Remove all duplicates from a given string in Python

a = []

a = input("Enter the String: ").split()
a = str(a[0])

p = None

c = []

d = ''

for i in range (0, len(a)-1, 1) :
    if a[i] != p :
        c += a[i]
        p = a[i]
for i in range (0, len(c), 1) :
    d += c [i]
print(d)