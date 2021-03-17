#Given a string, find all the duplicate characters which are similar to each others.

from collections import Counter

List = [-1 ,-1 ,1, 2]

word_length = Counter(List)

for A, B in word_length.items():
    if B > 1:
        print(f"{A} is happeing {B} times")
