#take one unsorted array and store (write) it into "file1.txt" file
Arr = [2,4,7,9,4,5,7,8]
file = open('file1.txt','w')
for i in Arr:
    file.write('%s\n' % i)
    
# Read Array from "file1.txt" sort it and print it in Ascending order
file = open('file1.txt','r')
file = sorted(Arr)
print(file)

