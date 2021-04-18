
# Program 1 : Write a Python program to check whether it follows the sequence given in the patterns array.Pattern example:
# For color1 = ["red", "green", "green"] and patterns = ["a", "b", "b"]
# the output should be samePatterns(color1, patterns) = true;
# For color2 = ["red", "green", "greennn"] and patterns = ["a", "b", "b"]
# the output should be samePatterns (strings, color2) = false.
def pattern():
    pattern=["a","b","c"]
    color=["red","blue","green"]
    if(len(color) != len(pattern)):
        print("false")
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
        print("false") 
    else:
        print("True")
pattern()                     #OUTPUT:True