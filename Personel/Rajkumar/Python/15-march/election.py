a = ["john", "johnny", "jackie",
     "johnny", "john", "jackie",
     "jamie", "jamie", "john",
     "johnny", "jamie", "johnny"]

cand = set(a)
print(a)
for cand in set(a):
    print(cand, a.count(cand))


import collections
c = collections.Counter(a)
print(c)
print(c.most_common(1))