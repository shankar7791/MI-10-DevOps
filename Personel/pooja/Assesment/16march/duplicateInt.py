list = [1, 2, 3, 4, 5, 6, 7, 2, 4, 6, 9, 1]
duplicates = []
uniqItems = {}
for x in list:
    if x not in uniqItems:
        uniqItems[x] = 1
    else:
        if uniqItems[x] == 1:
            duplicates.append(x)
        uniqItems[x] += 1

print(duplicates)
