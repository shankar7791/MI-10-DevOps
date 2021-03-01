n = int(input("enter the number of element)")

list=[]

i=1

while i <= n:
    j=int(input(f'enter {i} number of list:'))
    list.append(j)
    i += 1
if list[0] == list[len(list)-1]:
    print(True)
else:
    print(False)
