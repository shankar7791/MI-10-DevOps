def sum(dict, dict2):
    sum1 = 0
    sum2 = 0
    for i in dict :
        sum1 += dict[i]
    print(sum1)

    for j in dict2 :
        sum2 += dict2[j]
    print(sum2)

dict = {'a': 100, 'b':200, 'c':300}
dict2 = {'x': 25, 'y': 18, 'z': 45}
sum(dict, dict2) 