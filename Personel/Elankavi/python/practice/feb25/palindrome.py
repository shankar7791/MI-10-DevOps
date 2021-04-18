n=int(input("Enter the number : "))
tem = n
rev =0
while(n>0):
    a = n % 10
    rev =rev *10 + a
    n = n//10
print(rev)
if(tem == rev):
    print("palindrome")
else:
    print("not a palindrome")