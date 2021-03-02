#Palindrome number check

def palindrome():
    num =int(input("Enter the number :"))
    temp=num
    rev=0
    while(num>0):
         sum=num%10
         rev=rev*10+sum
         num=num//10
    if(temp==rev):
          print("Entered number is a palindrome")
    else:
          print("Entered number is not a palindrome")
palindrome()