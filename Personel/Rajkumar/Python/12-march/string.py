#Convert a list of characters into a string
a=input("Enter the chracter : ")
b=list(a)
c=" "
print("your list of character  : ",b)
for x in b:
    c+=x

print("Your string character : ",c)