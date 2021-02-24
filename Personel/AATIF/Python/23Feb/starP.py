num = int (input("Enter the Number: "))
row = 0
while row < num :
    star = row + 1
    while star > 0 :
        print("*", end=" ")
        star = star-1
    row = row + 1
    print()

row = 0
while (row <= num) :
    star = num
    while (star >= row) :
        print("*", end=" ")
        star -= 1
    row += 1
    print()