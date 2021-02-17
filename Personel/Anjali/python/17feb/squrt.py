num=int(input("Enter the number"))

sqrt=num/2
temp=0

print("number is:",num)
while sqrt !=temp :
    temp=sqrt
    sqrt=(num/temp+temp)/2
print("The square root is:", sqrt)