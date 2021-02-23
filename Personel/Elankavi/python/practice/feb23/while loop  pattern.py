#print the following pattern using loop 
# a)      *
#         **
#         ***
#         ****
#
# b)      *
#        ***
#       ***** 
#        ***
#         *   

i = 1
print("a)")

while i<=4:
    c = "*"*i
    print(c)
    i=i+1


j = 2
i =1
print("b)")
while i>=1:
    a= " "*j+"*"*i+" "*j                            
    print(a)                                       
    i = i+2                                        
    j=j-1
    if(i >5):
        break
i =3
j =1
while i>=1:
    b= " "*j+"*"*i+" "*j
    print(b)
    i = i-2
    j = j+1
   
