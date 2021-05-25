# Problem Statement :
# 1. take one unsorted array and store (write) it into "file1.txt" file
# 2. Read Array from "file1.txt" sort it and print it in Ascending order


#Initialize array     
arr = [5, 2, 8, 7, 1]    
arr1=[]    

# opening and writing original array into a text file
print('opening and writing original array into a text file \n')
file = open('arrsort.txt','w')
for element in arr:
    file. write('%s\n' % element )
print("File written successfully \n")
file. close()

# reading the contents of text file
print('reading the contents of text file \n')
file0=open('arrsort.txt','r')
print(file0.read())
file0.close()

#Displaying elements of original array and sorting
print('Displaying elements of original array and sorting \n')
file1=open('arrsort.txt','r') 
for line in file1:
    temp = line.split()
    for i in temp:
      arr1.append(i)
file1.close()
print('original contents: ', arr1)
arr1.sort()
print('sorted elements: ',arr1)
     

print('\n opening and writing sorted array into a text file ')
file2 = open("arrsort.txt", "w")
for i in arr1:
    file2.write(i)
    file2.write(" ")
print("File written successfully \n")
file2.close()

print('reading the contents of text file after sorting')
file3= open('arrsort.txt', 'r')
print('after sort file: ',file3.read())
file3.close()

