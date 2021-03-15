#Dictionary and counter in Python to find winner of election
from collections import Counter 
L = ["Congress", "BJP", "Congress", "BJP", "BJP", "BJP", "BJP"]
d = dict(Counter(L))
srt = sorted(d.items(), key= lambda x:x[1])
print("winner of election is", srt[-1][0])

