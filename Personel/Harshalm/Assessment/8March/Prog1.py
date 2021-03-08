# Write a Python program to print alphabet pattern 'A'


for rows in range(7):
    for cols in range(5) :
        if rows == 0 and cols == 1 or rows == 2 and cols == 1 :
            print("*", end = "")
        elif rows == 0 and cols == 0 or cols == 2 or cols == 1 :
            print("*", end = "")
        else :
            print("*", end = "")
print()
