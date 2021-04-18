#print odd numbers using continue 

a = int(input("Enter how much odd number you want "))

i = 0
while i < a :
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)