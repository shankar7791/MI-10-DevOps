# Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.


a=input("Enter the first string : ")
b=input("Enter the second string : ")
c=b[:2]+a[2:]
d=a[:2]+b[2:]
print(c +" "+ d)
