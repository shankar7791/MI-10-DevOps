# implementing hash function

# create an empty hashtable
hash_table=[None]*10

    # hashing function
def hashing(key):
    
        return key % len(hash_table)

# insert data into hash table
def insert(hash_table, key, value):
    i = hashing(key)
    if hash_table[i] is not None:
            # This index already contain some values.
            # This means that this add MIGHT be an update
            # to a key that already exist. Instead of just storing
            # the value we have to first look if the key exist.
        for kvp in hash_table[i]:
                # If key is found, then update
                # its current value to the new value.
            if kvp[0] == key:
                kvp[1] = value
                break
        else:
                # If no breaks was hit in the for loop, it 
                # means that no existing key was found, 
                # so we can simply just add it to the end.
            hash_table[i].append([key, value])
    else:
            # This index is empty. We should initiate 
            # a list and append our key-value-pair to it.
        hash_table[i] = []
        hash_table[i].append([key, value]) 

def display_hash(hash_table):
    
    for i in range(len(hash_table)):
        print(i, end = " ")
        if hash_table[i] != None:  
            for j in hash_table[i]:
                
                print("-->", end = " ")
                print(j, end = " ")
                
        print()




insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'us')
insert(hash_table, 37, 'uk')
insert(hash_table, 43, 'india')
insert(hash_table, 50, 'china')
display_hash(hash_table)