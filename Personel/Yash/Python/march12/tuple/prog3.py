# Program 3 : Remove empty tuples from a list


tuples = [(), ('yash',97), (), ('abc', 'xyz',45), ('',''),()] 
tuples_new = filter(None, tuples) 
print(list(tuples_new))