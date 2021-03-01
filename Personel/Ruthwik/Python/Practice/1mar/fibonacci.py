n1 = int(input("Enter the starting number : "))
n2 = int(input("Enter the second number : " ))
n = int(input("enter the range : "))
t=0

for i in range(n1, n2):
    print(n1)
    sum = n1 + n2
    n1 = n2
    n2 = sum

print("\n second loop \n")

for i in range(n):
    print(n)
    sum = n + t
    t = n
    n = sum