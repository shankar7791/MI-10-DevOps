#Given a string, find all the duplicate characters which are similar to each others.

from collections import Counter

word = str(input("Enter a Word : "))

word_length = Counter(word)

for A, B in word_length.items():
    if B > 1:
        print(f"{A} is happeing {B} times")

