#Print anagrams together in Python using List and Dictionary

def anagram(words):  
      
    dict = {}  
  
    for strVal in words:  
          
  
        key = ''.join(sorted(strVal))  
     
        if key in dict.keys():  
            dict[key].append(strVal)  
        else:  
            dict[key] = []  
            dict[key].append(strVal)  

    output = ""  
    for key,value in dict.items():  
        output = output + ' '.join(value) + ' '
  
    return output  
  
words=['cat', 'dog', 'tac', 'god', 'act']  
print (anagram(words))

