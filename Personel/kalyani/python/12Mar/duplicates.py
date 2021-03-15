#python groupby method to remove all the consective duplicate :

from itertools import groupby  
def removeAllconsective(input):
result=[]
for(key , group)in groupby (input):
result.append(key)
print('' . join(result))
    
#driven program
if __name__==" __main__":
    input = ' aaaaabbbbb'
    removeAllconsecutive(input)