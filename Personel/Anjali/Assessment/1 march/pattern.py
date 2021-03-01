rows = int(input("Enter the Number of Rows  : "))

i = rows
j=rows
while(i >= 1):
    j = i
    while(j >= 1):      
        print(j, end = '  ')
        j=j-1
    print()
    i=i-1
