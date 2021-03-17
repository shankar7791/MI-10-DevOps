a = int(input("Enter a number integers in list: "))
ls = []
for i in range(0, a):
    ele = int(input())
    ls.append(ele)
print("Given List: ", ls)

ls2 = []
for j in range(0, len(ls)):
    for k in range(j+1, len(ls)):
        if ls[j] == ls[k]:
            ls2.append(ls[k])
print("Duplicates from a List: ", ls2)