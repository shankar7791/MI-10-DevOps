from collections import Counter  
  
def winner(input):  
    vot = Counter(input)  
    dict = {}  
    for value in vot.values():  
        dict[value] = []  
    for (key,value) in vot.items():  
        dict[value].append(key)  
    mV = sorted(dict.keys(),reverse=True)[0]  
    return dict[mV]
  
input2 = input("enter the votes : ")
input = input2.split()
print("enter the votes are : ",input)
d = winner(input) 
if len(d)>1:  
    print ("winer is : ",sorted(d)[0]) 
else:  
    print ("winer is : ",(d[0]) ) 