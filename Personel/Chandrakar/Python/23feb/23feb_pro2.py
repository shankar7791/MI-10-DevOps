#Write a Python program to construct the following pattern, using a nested while loop
a=1
while(a>0):
    print("*"*a)
    a=a+1
    if(a==6):
        break
a=4
while(a<=4):
    print("*"*a)
    a=a-1
    if(a==0):
        break
        