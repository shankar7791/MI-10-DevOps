#check count of vowels in string
def count(str):
    count1=0
    for i in str:
        if (i=='a' or i=='e'or i=='i'or i=='o'or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            count1=count1+1
    print(count1)
str=input("Enter the string")
count(str)