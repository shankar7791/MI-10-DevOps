# Program 4 : Write a function which implements the Pascal's triangle using recursive function


num = int(input('Enter the rows : '))

def RecPascal(n, m=1, prev=[]):
    if m > n+1:
        return []
    elif m == 1:
        return RecPascal(n, m+1 , [1])
    else:
        return [prev] + RecPascal(n, m+1, calculate(prev))

def calculate(prev):
    res = [0]*(len(prev)+1)
    res[0], res[-1] = 1, 1
    for i in range(0,len(res)):
        if res[i] == 0:
            res[i] = prev[i-1] + prev[i]
    return res

for line in RecPascal(num):
    print(line) 