'''For color1 = ["red", "green", "green"] and patterns = ["a", "b", "b"]
the output should be samePatterns(color1, patterns) = true;
For color2 = ["red", "green", "greennn"] and patterns = ["a", "b", "b"]
the output should be samePatterns (strings, color2) = false.
'''


pattern=["a","b","c"]
color=["red","blue","green"]
if(len(color) != len(pattern)):
    print("false")
dict1={}
set1=set()
set2=set()
for i in range(len(color)):
    set2.add(color[i])
    set1.add(pattern[i])
    if pattern[i] not in dict1.keys():
        dict1[pattern[i]]=[]
    keys=dict1[pattern[i]]
    keys.append(color[i])

if len(set1) != len(set2):
    print("false") 
else:
    print("True")
