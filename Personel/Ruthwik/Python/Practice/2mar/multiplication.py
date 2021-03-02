#To print multiplication table pattern

n = int(input("Enter the number of rows "))
def mul(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # multiplication current column and row
            print(i * j, end='  ')
        print()

mul(n)