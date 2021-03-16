#python programn to interchange the first and last element in a list 

def interchange():
    n=[1,2,3,4,5]
    temp=n[0]
    n[0]=n[-1]
    n[-1]=temp
    print(n)
interchange() 