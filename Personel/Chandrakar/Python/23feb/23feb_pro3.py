# Write a Python program that accepts a word from the user and reverse it.
a=input("Enter the word : ")
b = ''
i = len(a)-1
while i >= 0 :
    b = b + a[i]
    i = i -1
print(b)    
