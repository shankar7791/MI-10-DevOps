num=int(input("Enter number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
    
if(temp==rev):
    print("The number is a palindrome!")
else:
    remainder = num % 10  
    rev = (rev * 10) + remainder  
    num = num // 10  
  
  
    print(f"{rev} reverse number ")  