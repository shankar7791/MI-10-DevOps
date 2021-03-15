#Remove empty tuples from a list

def Remove(tuples): 
    tuples = filter(None, tuples) 
    return tuples 
 
tuples = [(), ('avi','23','18'), (), ('ravi', '31'),  
          ('krishna', '45'), ('',''),()] 
print(Remove(tuples))