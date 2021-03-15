#convert a list of character into string :

a=input("Enter the chracter : ")
b=list(a)
n=" "
print("your list of character  : ",b)
for x in b:
    n+=x

print("Your string character : ",n)