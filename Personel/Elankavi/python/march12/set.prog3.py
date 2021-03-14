#Remove item from set untill set not become empty set

def empty():
    a=set([1,2,3,4,5,6,7,8])
    b=len(a)
    i=0
    while(b>=0):
        a.discard(i)
        print(a)
        b-=1
        i+=1
    
empty()