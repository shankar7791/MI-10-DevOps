# remove the all duplicate from the given string:

def duplicate():
    s=("Elaannkavii")
    s1=sorted(s)
    print(type(s1))
    dup=[]
    for i in s1:
        if i not in dup:
            dup.append(i)
        else:
            pass
    print(tuple(dup))
duplicate()