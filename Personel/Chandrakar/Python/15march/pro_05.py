def dublicat(l):
    k = [] 
    for i in l: 
        if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
            k.append(i)         
    print("after removing : ",' '.join(k))  
s = "Python is great and Java is also great"
print("befor the removing sentence : ",s)
l = s.split() 
dublicat(l)