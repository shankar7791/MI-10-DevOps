# Python program to interchange first and last elements in a list
def swap():
    n=int(input("Enter the number of element in list   "))
    list=[]
    for x in range(0,n):
        ele=input("Enter element  ")
        list.append(ele)
    print(f"Befor swap list  {list}  ")
    temp=list[0]
    list[0]=list[n-1]
    list[n-1]=temp
    print(f"After swap list  {list}  ")
swap()