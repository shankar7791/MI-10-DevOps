def hash_key( key, m):
    return key % m


m = 7

print(hash_key(3,m))
print(hash_key(2,m))
print(hash_key(9,m))
print(hash_key(11,m))
print(hash_key(7,m))