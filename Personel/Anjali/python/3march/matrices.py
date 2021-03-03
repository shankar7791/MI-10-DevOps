row=int(input("how many rows"))
col=int(input("how many col"))

l=[[i for i in range(row)]for j in range(col)]

print("enter the element")
for i in range(row):
	for j in range(col):
		l[i][j]=int(input())
for i in range(row):
	for j in range(col):
		print(l[i][j],end='\t')
	print('\n')