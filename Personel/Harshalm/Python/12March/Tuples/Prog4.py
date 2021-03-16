#Reversing a Tuple

def tup_rev(tuples):
    
    nt = tuples[::-1]

    return nt

i = tuple(input('Enter a tuple : '))
print(i)

print(tup_rev(i))
