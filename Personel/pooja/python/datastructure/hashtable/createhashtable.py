def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i,end = "")
          
        for j in hashTable[i]:
            print("---->",end = "")
            print(j,end = "")
              
        print()

HashTable = [[] for _ in range(10)]
def hashing(keyvalue):
    return keyvalue % len(HashTable)


def insert (HashTable , keyvalue ,value):
    hash_key = hashing(keyvalue)
    HashTable[hash_key].append(value)

insert(HashTable,15,'pooja')
insert(HashTable,25,'disha')
insert(HashTable,35,'prasad')
insert(HashTable,41,'Abhi')
insert(HashTable,5,'amruta')

display_hash(HashTable)