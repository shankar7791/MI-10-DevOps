#pascal triangle


num = int(input('Enter the rows : '))

def RecPascal(y, x=1, prev=[]):
    if x > y+1:
        return []
    elif x == 1:
        return RecPascal(y, x+1 , [1])
    else:
        return [prev] + RecPascal(y, x+1, calculate(prev))

def calculate(prev):
    res = [0]*(len(prev)+1)
    res[0], res[-1] = 1, 1
    for i in range(0,len(res)):
        if res[i] == 0:
            res[i] = prev[i-1] + prev[i]
    return res

for line in RecPascal(num):
    print(line) 
