# implementing hash function with chaining

# create an empty hashtable
hash_table=[[] for _ in range(10)]

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
    print('\nSize | Keys and Values')
    print("") 
    for i in range(len(hash_table)):
        print(i, end = " ")
        if hash_table[i] != None: 
            for j in hash_table[i]:
                
                print("  |-->", end = " ")
                print(j, end = " ")
                
        print()




menu = {}
menu['1']="Add Data" 
menu['2']="Print Data"
menu['3']="Exit"

while True:
    options=menu.keys()
    
    print ("\nMENU")
    print("======================\n")
    for entry in options: 
      print (entry, menu[entry])
    print("")
    selection = input("\nPlease Select:\n")

    if selection == '1' :
        print ("\nAdding Data\n") 
        length = int(input("Enter the number of data you want for your Hash Table : \n"))
        for counter in range(1,length+1) :
        
            key=int(input('enter the key : '))
            value=input('enter the value :')
            ht=hash_table
            insert(ht,key,value)


    elif selection == '2' :
        display_hash(hash_table)

    elif selection == '3':
        exit()
    
    else: 
      print ("\nUnknown Option Selected!") 