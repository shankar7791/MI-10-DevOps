#to get a single string from a two stringand swap the first two character 

a=input("Enter the first string : ")
b=input("Enter the second string : ")
c=b[:2]+a[2:]
d=a[:2]+b[2:]
print(c +" "+ d)
