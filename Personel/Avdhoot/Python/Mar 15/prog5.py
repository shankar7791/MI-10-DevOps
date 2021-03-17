'''Remove all duplicates words from a given sentence
        Examples:
        Input : Geeks for Geeks
        Output : Geeks for
        Input : Python is great and Java is also great
        Output : is also Java Python and great
'''
def unique(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

a = input("Enter a Sentence: ")
print(' '.join(unique(a.split())))