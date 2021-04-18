
num = int(input("Enter the Number:"))
c = 0
while num != 0:
    num //= 10
    c+= 1
print(f"Total digits count is ={c} ")