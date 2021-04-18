#Python program that accepts a word from the user and reverse it.

a=input("Enter a word :")
rev_a=''

length=len(a)-1

while length>=0:
    rev_a = rev_a + a[length]
    length=length-1

print("Entered word is: ",a)
print("The reversed word is : ",rev_a)