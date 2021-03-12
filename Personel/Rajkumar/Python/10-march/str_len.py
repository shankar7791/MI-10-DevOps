n=input("Enter the string : ")
def len(n):
    l=len(n)
    print(f"The length of {n} is {l}")
def rev(n):
    r=n[::-1]
    print(f"The reverse of {n} is {r}")
def pali(n):
    r=n[::-1]
    s=n[::1]
    if(r==s):
        print(f"The {n}ia a palindrome")
    else:
        print(f"The {n} is not a palindrome ")
def sym(n):
    b=len(n)
    c=1
    if b%2:
        mid=b//2 +1
    else:
        mid=b//2
    start=0
    start1=mid
    while(start < mid and start1 < b):
        if(n[start])==n[start1]:
            start +=1
            start1 +=1
        else:
            c=0
            break
    if(c==0):
        print(f"The {n} is not a symmetric")
    else:
        print(f"The {n} is  a symmetric")
    print()

len(n)
rev(n)
pali(n)
sym(n)

from itertools import permutations
p= permutations(n)
print(f"The permutation of {n} is ")
for i in list(p):
    print("".join(i),end=" ")
from itertools import combinations
c=combinations(n,2)
print(f"\n The combination of {n} is : ")
for i in list(c):
    print("".join(i),end =" ")
print()

def anagram(n):
    b=input("Enter another string : ")
    if(sorted(n)==sorted(b)):
        print(f"The strings {n} and  {b} are anagram")
    else:
        print(f"The string {n} and {b} are not anagram")
anagram(n)
