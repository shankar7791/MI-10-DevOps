# To print the duplicate from a list of integers

def duplicate():
    n=[1,2,3,3,2,4,56,6,3,4,5]
    
    dup=[]
    dup2=[]
    for i in n:
        if i not in dup:
            dup.append(i)
        else:
            dup2.append(i)
    print(dup2)
duplicate()