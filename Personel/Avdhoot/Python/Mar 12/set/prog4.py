#Python set to check if string is panagram

a = input("Enter the string : ")

l = set({})
for i in a:
    if ( i >= ('a') and i <= ('z')):
        l.add(i)
c = len(l)
if(c == 26):
    print("Panagram")

else:
    print("Not a Panagram")
