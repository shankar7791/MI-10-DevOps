#To print all prime numbers in given range

n1 = int(input("Enter the starting number of the range : "))
n2 = int(input("Enter the last number of the range : " ))

for n in range(n1, n2+1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)