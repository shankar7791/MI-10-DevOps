#Program to print duplicates from a list of integers
def dup():
    n=int(input("enter the number for list"))
    list=[]
    for x in range(0,n):
        ele=int(input("Enter the number"))
        list.append(ele)
        size=len(list)
    print(f"{list} is list")
    for i in range(size):
        for j in range(i+1,size):
            if list[i]==list[j]:
                print(f"{list[i]} is duplicate element")
print()
dup()