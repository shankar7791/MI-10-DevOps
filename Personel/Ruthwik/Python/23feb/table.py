#Python program to create the multiplication table of a number

n= int(input("Enter the number of which you want the table :"))
i=1
t=0

while i<=10:
    t=n*i
    print(f"{n}*{i} = {t}")
    i=i+1