#Python program that accepts a string and calculate the number of digits and letters.

a = input("Enter a string: ")
n=0
w=0
i=0
l=len(a)
while i<l:
    if a[i].isdigit():
        n =n +1
    elif a[i].isalpha():
        w = w +1
    else:
        print(f"Other than letter and digit = {a[i]}")
    i=i+1

print(f"Digits are : {n}")
print(f"Letters are : {w}") 