list1 = [1,2,4,5,"Teju",'a','b']

def ListEx(l):
    for x in l:
        if x == "Teju":
            continue
        print(x)

ListEx(list1)