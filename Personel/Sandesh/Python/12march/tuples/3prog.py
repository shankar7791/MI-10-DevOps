#Remove empty tuples from a list

list=[(),(),("sandesh"),(""),("patekar"),(),("sandesh , 01"),("333"), ()]
A=filter(None,list)
print(tuple(A)) 