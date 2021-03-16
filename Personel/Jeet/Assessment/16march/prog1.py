n = int(input('enter list size:'))
lst = []
for i in range(1,n+1):
    lst.append(int(input(f'Enter {i} element:')))
print('before swappig',lst)
t = lst[0]
lst[0]=lst[len(lst)-1]
lst[len(lst)-1]=t
print('after swapping:',lst)
