n = int(input('enter list size:'))
lst = []
dlst = []
for i in range(1,n+1):
    a=int(input(f'Enter {i} element:'))
    if a in lst:
        dlst.append(a)
        lst.append(a)
    else:
        lst.append(a)
print('duplicate values:',dlst)
