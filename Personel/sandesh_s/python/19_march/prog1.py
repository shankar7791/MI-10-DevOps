# Write a Python program to check whether it follows the sequence given in the patterns array.


def pattern() :
    pat = ["a","b","c"]
    col = ["red","blue","green"]

    if len(col) != len(pat) :
        print("false")
    cdict = {}
    pset = set()
    cset = set()

    for i in range(len(col)) :
        cset.add(col[i])
        pset.add(pat[i])

        if pat[i] not in cdict.keys() :
            cdict[pat[i]]=[]
        keys = cdict[pat[i]]
        keys.append(col[i])

    if len(pset) != len(cset) :
        print("false")
    else:
        print("True")
pattern()            
