#Print anagrams together in Python using List and Dictionary

def allAnagrams(input) :
    dict = {}
    for strVal in input :
        key = " ".join(sorted(strVal))

        if key in dict.keys() :
            dict[key].append(strVal)
        else :
            dict[key] = []
            dict[key].append(strVal)

    result = " "
    for key, value in dict.items() :
        result = result + " ".join(value) + " "
    return result

str = [item for item in input("Enter the list of items :-").split()]
print(str)
allAnagrams(str)
