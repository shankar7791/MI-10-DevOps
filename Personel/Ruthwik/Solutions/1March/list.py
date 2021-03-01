#Given a list of numbers, return True if first and last number of a list is same.

n=input("Enter a list of numbers :")
l=list(n)

print("The original list is :",l)

if l[0] == l[-1]:
    print(True)
else:
    print(False)