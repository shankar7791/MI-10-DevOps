# print anagrams together in python using list and dictionary

def Anagram():
    w=('cat', 'dog', 'tac', 'god', 'act')
    dict={}
    for word in w:
        sortedword="".join(sorted(word))
       
        

        if (sortedword not in dict):
            dict[sortedword]=[word]
            
        else:
            dict[sortedword].append(word)
            
        result=[]
        for item in dict.values():
            
            result.append(item)
    print(result)
      
Anagram()