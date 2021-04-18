# Remove items from set until set not become empty set

def remove(set1):
    while set1:
        set1.pop()
        print(set1)
set1 = set(['a','b',1,2,'c'])
remove(set1)
