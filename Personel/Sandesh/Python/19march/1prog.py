# write a Pythoon program to check whether it  follows the sequence given in the pattens array
"""
Pattern example:
For color1 = ["red", "green", "green"] and patterns = ["a", "b", "b"]
the output should be samePatterns(color1, patterns) = true;
For color2 = ["red", "green", "greennn"] and patterns = ["a", "b", "b"]
the output should be samePatterns (strings, color2) = false."""

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