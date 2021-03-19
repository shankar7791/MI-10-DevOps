''' Write a Python program to check whether it follows the sequence given in the patterns array.
    Pattern example:
    For color1 = ["red", "green", "green"] and patterns = ["a", "b", "b"]
    the output should be samePatterns(color1, patterns) = true;
    For color2 = ["red", "green", "greennn"] and patterns = ["a", "b", "b"]
    the output should be samePatterns (strings, color2) = false
'''

#...................................................................................................................................


def Patterns(colours, p1):    

    if len(colours) != len(p1):
        return False    
    
    dict1 = {}
    set1 = set()
    set2 = set()    
    
    for i in range(len(p1)):
        set1.add(p1[i])
        set2.add(colours[i])
    
        if p1[i] not in dict1.keys():
            dict1[p1[i]] = []

        keys = dict1[p1[i]]
        keys.append(colours[i])
        dict1[p1[i]] = keys

    if len(set1) != len(set2):
        return False   

    for values in dict1.values():

        for i in range(len(values) - 1):
    
            if values[i] != values[i+1]:
                return False

    return True

print("samePatterns(color1, patterns): ", Patterns(["red", "green", "green"], ["a", "b", "b"])) 

print("samePatterns (strings, color2): ", Patterns(["red", "green", "greennn"], ["a", "b", "b"]))