# Program 3 : Given a list of numbers, return True if first and last number of a list is same

# lst = ["yash",1,2,3,True,"abc","yash"]
# if lst[0] == lst[len(lst)-1]:
#     print(True)
# else:
#     print(False) 

n=input("Enter a list of numbers :")
l=list(n)
print("The original list is :",l)
if l[0] == l[-1]:
    print(True)
else:
    print(False)