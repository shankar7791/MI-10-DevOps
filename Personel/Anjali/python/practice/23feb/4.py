num1=int(input("Enter the start number"))
num2=int(input("Enter the end number"))
count_even=0
count_odd=0

while num1<=num2:
    if num1%2==0 :
        count_even=count_even+1
    else :
        count_odd=count_odd+1
    num1 = num1 + 1
print(f"{count_even} Even number count")
print(f"{count_odd} odd number count")