# while loop break 
num = int(input("enter the number = "))
sum = 0
c   = 0
while c < num :
    sum = sum + c
    c   = c   + 1
    if c == 6 :
        break
print("sum of ",c,"integer is : ",sum)         