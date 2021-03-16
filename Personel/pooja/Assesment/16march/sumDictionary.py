def sum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i
    return sum


#dict = {'a': 100, 'b': 200, 'c': 300}
dict = {'x': 25, 'y': 18, 'z': 45}
print(sum(dict))
