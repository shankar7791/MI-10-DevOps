from collections import OrderedDict


def removeDuplicate(str1):
    return ''.join(OrderedDict.fromkeys(str1))


print(removeDuplicate('greeksforgreeks'))
