# Remove empty tuples from a list

def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples

tuples = [(), ('Aatif','Avdhoot','Anjali','Chandrakar','Chetan'), ()]
print(Remove(tuples))
