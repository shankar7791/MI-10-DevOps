from itertools import groupby


def ConsecAll(string):

    result = []
    for (key, group) in groupby(string):
        result.append(key)
    print(''.join(result))


string = input("enter the string")
ConsecAll(string)
