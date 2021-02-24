
# logical operators 

x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))

if x < y and y > x :
    print(f"Sum = ",x + y) 

elif x > y or y < x :
    print(f"Sub = ", x - y) 

else :
    print(f"{x} and {y} both are equal  ")

print(not(x > 10 and y < 50))
