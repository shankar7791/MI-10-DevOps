#To check the string is panagram or not

def panagram():
    a=input("Enter the string : ")
   
    l=set({})
    for i in a:
        if ( i >= ('a') and i <= ('z')):
            l.add(i)
    c=len(l)
    if(c==26):
        print("panagram")

    else:
        print("not a panagram")
panagram()
