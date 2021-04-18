num=int(input("Enter a number: "))
rev=0
p=num
while (num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(rev==p):
    print("Given numbe is palindrom")
else :
    print("Given numbe is not palindrom")

