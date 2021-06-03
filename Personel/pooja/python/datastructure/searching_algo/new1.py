def check(s1,s2):
    a=len(s1)
    b=len(s2)
    i=j=0
    while j<a and i<b:
        if s1[j] == s2[i]:
            j+=1
        i+=1
    return j==a
def main():
    v=input()
    n=int(input())
    x=[]
    for i in range(n):
        x.append(input())
    for i in x:
        print("POSITIVE" if check(i,v) else "NEGATIVE")  
s1 = input("enter string for s1")
s2 = input(" enetr string for s2")
main()
check(s1,s2)