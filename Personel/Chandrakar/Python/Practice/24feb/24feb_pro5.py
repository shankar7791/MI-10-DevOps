a = int(input("enter the number :"))
b = int(input("enter the number :"))
list = [1, 2, 3, 4, 5 ]

if ( a in list ):
   print(a,"in a list")
else:
   print(a,"is not available in list")

if ( b not in list ):
   print (b,"is not available list")
else:
   print (b,"is available in  list")