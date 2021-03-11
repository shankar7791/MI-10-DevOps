#string _ to perform operations
#1.Length of string 2.Revrse 3.palindrome 4.symmetrical 5.permutation and combination 6.anagram


a=input("Enter the string : ")
def length(a):
    l=len(a)
    print(f"The length of {a} is {l}")
def rev(a):
    r=a[::-1]
    print(f"The reverse of {a} is {r}")
def palindrome(a):
    r=a[::-1]
    s=a[::1]
    if(r==s):
        print(f"The {a}ia a palindrome")
    else:
        print(f"The {a} is not a palindrome ")
def symmetrical(a):
    b=len(a)
    c=1
    if b%2:
        mid=b//2 +1
    else:
        mid=b//2
    start=0
    start1=mid
    while(start < mid and start1 < b):
        if(a[start])==a[start1]:
            start +=1
            start1 +=1
        else:
            c=0
            break
    if(c==0):
        print(f"The {a} is not a symmetric")
    else:
        print(f"The {a} is  a symmetric")
    print()

length(a)
rev(a)
palindrome(a)
symmetrical(a)

from itertools import permutations
p= permutations(a)
print(f"The permutation of {a} is ")
for i in list(p):
    print("".join(i),end=" ")
from itertools import combinations
c=combinations(a,2)
print(f"\n The combination of {a} is : ")
for i in list(c):
    print("".join(i),end =" ")
print()

def anagram(a):
    b=input("Enter another string : ")
    if(sorted(a)==sorted(b)):
        print(f"The strings {a} and  {b} are anagram")
    else:
        print(f"The string {a} and {b} are not anagram")
anagram(a)


