#list
n = int(input('Enter a no. of element in list:'))
lst = []
i = 1
while i <= n:
    j = int(input(f'Enter {i} number of list:'))
    lst.append(j)
    i +=1
if lst[0] == lst[len(lst)-1]:
    print(True)
else:
    print(False) 