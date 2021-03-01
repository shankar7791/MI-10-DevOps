#Reverse right angle number pattern

n = int(input("Enter rows : "))
i = 1

while i <= n :
    j = n
    while j >= i:
        print(j, end=" ")
        j -= 1
    print()
    i += 1