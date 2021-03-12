


#To check the given string is heterogram or not

def heterogram():
    str = input("Enter the string : ")
    b = len(str)
    l=set({})
    for i in str :
        if ( i >= ('a') and i <= ('z')):
            l.add(i)
    c = len(l)
    if c == b :
        print("Heterogram")

    else:
        print("not a hetrogram")
heterogram()