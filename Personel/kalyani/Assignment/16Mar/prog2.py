# Program to print duplicates from a list of interger

list[ -1 , 1 , -1 , 8]
duplicatesitems= []
uniqitems = {}
for x in list:
    if x not in uniqitems:
        uniqitems[x] =1
    else:
        if uniqitems[x] == 1:
            duplicatesitems.append(x)
        uniqitems[x] += 1
print (duplicatesitems)