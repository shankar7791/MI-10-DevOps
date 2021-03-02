#  Write a Python program that accepts a sequence of lines  as input and prints the lines as output (all characters in lower case).

n=input("Enter the character : ")
for l in n:
    if n:
        h=n.lower()
        print("The string in lower case : ", h)
        c=n.upper()
        print("The string in upper case : ",c)
        break
