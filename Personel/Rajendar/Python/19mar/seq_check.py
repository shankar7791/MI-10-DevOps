# Write a Python program to check whether it follows the sequence given in the p array.

def sam_pat(c, p):
    if len(c) != len(p):
        return False
    sdict = {}
    pset = set()
    sset = set()
    for i in range(len(p)):
        pset.add(p[i])
        sset.add(c[i])
        if p[i] not in sdict.keys():
            sdict[p[i]] = []

        keys = sdict[p[i]]
        keys.append(c[i])
        sdict[p[i]] = keys

    if len(pset) != len(sset):
        return False

    for values in sdict.values():

        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False

    return True


pat = input("Enter a string : ")
l = pat.split(" ")
print('The entered list is :', l)

col = input("Enter a string : ")
k = col.split(" ")
print('The entered list is :', k)

print(sam_pat(k, l))
