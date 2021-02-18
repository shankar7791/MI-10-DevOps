#check the number is divisible by 5 or 11

num = int(input("Enter your number : "))
if(num % 5 ==0):
    print(num, "is divible by 5")
elif(num % 11 ==0):
    print(num, " is divible by 11")
else:
    print(num,"is not divisible by 5 & 11")