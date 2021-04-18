num=int(input("Enter a number: "))
rev=0;
while (num>0):
    rm=num%10
    rev=rev*10+rm
    num=num//10
print("Revers number is:",rev)
