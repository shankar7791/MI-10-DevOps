even=0
odd =0
n1=int(input("Enter the start no: "))
n2=int(input("Enter the end no: "))
num1=n1

while n1<n2:
    if(n1%2==0):
        even+= 1
    else:
        odd+= 1
    n1+= 1

print(f"Even Number of count is {even} form {num1} to {n2}")
print(f"\nOdd Number of count is {odd} form {num1} to {n2}")
