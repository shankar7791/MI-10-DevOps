def heterogram():
    a=input("Enter the string : ")
    b=len(a)
    l=set({})
    for i in a:
        if ( i >= ('a') and i <= ('z')):
            l.add(i)
    c=len(l)
    if(c==b):
        print("Heterogram")

    else:
        print("not a hetrogram")
heterogram()
