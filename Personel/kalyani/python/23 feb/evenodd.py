# WAP to count the no of even and odd no from a series of nos.

1 = int(input("Enter the first number"))

n2 = int(input("Enter the last number"))

count_even = 0

count_odd = 0

while n1 <= n2 :

    if n1%2 == 0 :
        count_even = count_even + 1
    else :
        count_odd = count_odd + 1
    n1 = n1 + 1

print(f"{count_even} Even number count")
print(f"{count_odd} odd number count")