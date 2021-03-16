def anagram(list1):
    dict = {}
    for i in list1 :
        key = ''.join(sorted(i))
        if key in dict.keys():
            dict[key].append(i)
        else :
            dict[key] = []
            dict[key].append(i)
    result = ""
    for key,value in dict.items():
        result = result + ' '.join(value) + ' '
    return result

list1 = ['cat','dog','tac','god','act']
print(anagram(list1)) 