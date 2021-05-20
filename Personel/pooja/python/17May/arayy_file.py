#create an empty array as input
# create file in write mode 
# write array into file
# close the file
# open file with read mode
# store file data into variable
# append list element into array
# sort array in ascending order
# print the array
# import  array as arr
# array_ = arr.array("i",[10,45,89,52,37,14,98])
# file= open("ps.txt","r")
# file.write("pooja ash nish fish wish")
# file.close()
# file1=open("file1.txt","r")

# def ascending_arr(val):
# val=list(input("Enter the list : "))
# writing into file
# f=open("demo1.txt","w")
# print(" values before sorting")
# for i in val:
#     print( i, end ="")
#     f.write(str(i))
# f.close()

# reading from file
# with open("demo1.txt","r") as f1:
    
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
    print(i,end=" " )
    f1.write(i)
f1.close()
    
    
     
# val=int(input("enter values :"))
# for i in val:
#     print(ascending_arr(i))


