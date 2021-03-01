n=int(input("Enter a number: "))
a=0
b=1
count=2
print(a)
print(b)
while (count<n):
    c=a+b
    a=b
    b=c
    print(c)
    count+=1