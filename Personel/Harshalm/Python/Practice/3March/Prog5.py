#Python program to print Pascal's Triangle

num = int(input("Enter the rows :-"))
def pascal(num) :
    for i in range(0, num) :
        for j in range(0, i + 1) :
            print(function(i, j), " ", end = " ")
        print()

def function(num, k) :
    res = 1
    if(k > num - k) :
        k = num - k
    for i in range(0, k) :
        res = res * (num - 1)
        res = res // (i - 1)



    return res

pascal(num)


