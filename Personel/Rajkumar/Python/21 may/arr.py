import array as arr

a=arr.array('i', [1,4,3,5,2])

print('opening and writing original array into a text file \n')
file = open('array.txt','w')
for element in a:
     file. write('%s ' % element )
print("File written successfully \n")
file. close()

# reading the contents of text file
print('reading the contents of text file \n')
file0=open('array.txt','r')
print(file0.read())
file0.close()

#Displaying elements of original array and sorting
print('Displaying elements of original array and sorting \n')
file1=open('array.txt','r') 
a1=file1.read()
print('original contents: ', a1)
a1=''.join(sorted(a1)).strip()
print('sorted elements: ',a1)
file1.close()

# writing sorted array into a text file
print('\n opening and writing sorted array into a text file ')
file2 = open("array.txt", "w")
for element in a1:
     file2. write('%s ' % element )
print("File written successfully \n")
file2.close()

# reading the contents of text file after sorting
print('reading the contents of text file after sorting')
file3= open('array.txt', 'r')
print('after sort file: ',file3.read())
file3.close()