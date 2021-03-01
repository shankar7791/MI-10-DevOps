n=input("Enter a list of numbers :")
l=list(n)

print("The original list is :",l)

if l[0] == l[-1]:
    print(True)
else:
    print(False)