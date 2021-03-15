
# Dictionary and counter in Python to find winner of election


a = ["a","b","c","a","b","a","b","c","b"]

cand = a
for cand in set(a) :
    print(cand,"=", a.count(cand))

import collections
c = collections.Counter(a)
print("The winner is : ")
print(*c.most_common(1))

