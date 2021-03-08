#Write a function which implements the Pascal's triangle using recursive function

def printPascal(n) :
    if n == 0 :
        return [1]

    else :
        line = [1]
        previousLine = printPascal(n - 1)

        for i in range(len(previousLine) - 1):
            line.append(previousLine[i] + previousLine[i + 1])

        line += [1]
        
    return line

n = int(input('enter no:'))
print(printPascal(n))