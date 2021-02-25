num = int(input("Enter number : "))
temp = num
rev=0 
while(num>0): 
    sum=num%10
    rev=rev*10+sum
    num=num//10
    
if(temp==rev):
    print("The number is Palindrome !!")
else: 
    remainder = num % 10 
    rev = (rev * 1) + remainder
    num = num //10
    print(f"{rev} reverse number ")
    print("The number not a palindrome !")