# Remove item from set untill set not become empty set

def empty():
    a=set([,2,3,4])
    b=len(a)
    i=0
    while(b>=0):
        a.discard(i)
        print(a)
        b-=1
        i+=1

empty() 
