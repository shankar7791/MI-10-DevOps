n=int(input("Enter a number: "))
t=n
rev=0
while n>0:
    rem=n%10
    rev=rev+rem*rem*rem
    n=n//10
if rev==t:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
