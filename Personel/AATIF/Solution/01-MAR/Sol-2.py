ls = []

num = int(input("Enter the number elements of list: "))

i=0
while i < num:
    ele = int(input("Enter the Elements: "))
    ls.append(ele)
    i = i + 1
print(ls)

ls1 = ls[0]
ls2 = ls[-1]

if ls1 == ls2 :
    print(True)
else :
    print(False)