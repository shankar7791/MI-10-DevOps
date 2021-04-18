# Python groupby method to remove all consecutive duplicates

from itertools import groupby
def removeAllCosecutive(string) :

    result = []
    for(key, group) in groupby(string) :
        result.append(key)
    print(''.join(result))

str = tuple(input("Enter the tuple :-"))
#print(str)
removeAllCosecutive(str)

