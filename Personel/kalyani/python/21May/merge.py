def mergesort(a):
    if len(a)>1:
        mid=len(a)//2
        L=a[:mid:]
        R=a[mid:]
        mergesort(L)
        mergesort(R)
        
        a.clear()
        while len(L)>0 and len(R)>0:
            if L(0)<= R(0):
                a.append(L[0])
                L.pop(0)
            else:
                a.append(R[0])
                R.pop(0)
        for i in L:
            a.append()
            
        for i in R:
            a.append()
            
            
a=[]
n=int(input( "Enter the upper limit :"))
for i in range(0,n):
    a.append(int(input(" Enter the element :")))
print(a)