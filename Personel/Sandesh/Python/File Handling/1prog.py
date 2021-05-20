# take one unsorted array and store (write) it into "file1.txt" file
Arr = [5,4,8,9,12,6,2,8]
file1 = open('file1.txt','w')
for i in Arr:
    file1.write('%s\n' % i)

#Read Array from "file1.txt" sort it and print it in Ascending order
file1 = open('file1.txt','r+')
file1= sorted(Arr)
print(file1)

