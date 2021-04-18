#Remove empty tuples from a list

def removeEmpty(tuples) :
    tuples = [t for t in tuples if t]
    return tuples

str = list(tuple(map(str,input().split())) for i in range(int(input("Enter Number of rows :-"))))
print(str)

print(removeEmpty(str))
