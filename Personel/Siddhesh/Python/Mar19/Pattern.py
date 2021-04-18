
#patterns

def pattern():
    pattern=["a","b","b"]
    color=["red","blue","greennn"]
    if(len(color) != len(pattern)):
        print(false)
    colordict={}
    patternset=set()
    cset=set()
    for i in range(len(color)):
        cset.add(color[i])
        patternset.add(pattern[i])
        if pattern[i] not in colordict.keys():
            colordict[pattern[i]]=[]
        keys=colordict[pattern[i]]
        keys.append(color[i])

    if len(patternset) != len(cset):
        print("false") 
    else:
        print("True")
pattern() 

