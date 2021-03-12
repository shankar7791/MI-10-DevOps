#Remove empty tuples from list

def remove(l):
    t = [ x for x in l if x]
    return t

l = [(),('q',2,3),('',''),("xantrons","ambersoft"),()]
print("Orignal list: ",l)
print("List after removing empty tuple: ",remove(l))
