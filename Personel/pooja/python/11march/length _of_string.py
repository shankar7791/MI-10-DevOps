import string
from itertools import permutations
import itertools
str = input("enter your string :")
print(len(str))  # length of string

str2 = str[::-1]   # reverse string
print(str2)

str3 = str[::-1]  # pallindrome or not
if str3 == str:
    print("string is pallindrome: ")
else:
    print(" string is not pallindrome")


n = len(str)  # symmetrica
count = 0

if n % 2:
    mid = n//2+1
else:
    mid = n//2

start1 = 0
start2 = mid

while(start1 < mid and start2 < n):
    if(str[start1] == str[start2]):
        start1 = start1 + 1
        start2 = start2 + 1
    else:
        count = 1
        break

if count == 0:
    print("The string is symmetrical")
else:
    print("The string is not symmetrical")

  # permutations
per = itertools.permutations(str)
for val in per:
    print(*val)

# combination

com = itertools.combinations(str, 2)
for val in com:
    print(*val)

# anagram string
s1 = 'listen'
if(sorted(str) == sorted(s1)):
    print("string is anagram")
else:
    print("not an anagram")
