def dub(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
        else:
            print("output_list : ","[",i,"]")
l=[-1,1,-1,8]
dub(l)
