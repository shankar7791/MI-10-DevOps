def pattern():
    pattern=["a","b","c","c"]
    color=["red","blue","green","green"]
    if(len(color) != len(pattern)):
        print("False")
    cdict={}
    pset=set()
    cset=set()
    for i in range(len(color)):
        cset.add(color[i])
        pset.add(pattern[i])
        if pattern[i] not in cdict.keys():
            cdict[pattern[i]]=[]
        keys=cdict[pattern[i]]
        keys.append(color[i])

    if len(pset) != len(cset):
        print("False") 
    else:
        print("True")
pattern()