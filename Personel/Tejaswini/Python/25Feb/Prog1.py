a=5
b=6
while b!=0:
    c=a&b
    a=a^b
    b=c<<1
print(f"Addition of two number ={a}")