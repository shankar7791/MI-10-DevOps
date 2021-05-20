ar=list(input("Enter the list : "))
f=open("file1.txt","w+")
print("Before Sorting")
for i in ar:
    print(i,end=" ")
    f.write(str(i))
f.close()
f1=open("file1.txt","r+")
d=f1.read()
print("\n After sorting")
data=sorted(d)
f1.write("\n")
for i in data:
    print(i,end=" ")
    
    f1.write(i)

f1.close()
    


