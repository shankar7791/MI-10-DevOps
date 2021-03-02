h=int(input("Enter a Integer value:-"))
j=1
for i in range(h,h//2,-1):
    print(' '*(i-(h//2)-1),' * '*j)
    j+=2
j-=4
for i in range(1,(h//2)+1,1):
    print(' '*i,' * '*(j))
    j-=2


