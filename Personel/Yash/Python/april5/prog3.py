f = open("demo.txt","r")
print(f.read())

# print(f.read(2)) #Return the first 2 characters of the file

# print(f.readline()) #return one line


# print(f.readline())
# print(f.readline())#return two line

# print(f.readlines()) #['Hi\n', 'hello\n', 'I am Yash']

# for x in f:
#   print(x) 

f.close()