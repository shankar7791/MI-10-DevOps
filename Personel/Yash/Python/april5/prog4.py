f = open("demo.txt", "a") #Open the file "demo.txt" and append the content to the end of the file
f.write("Now the file has more content")
f.close()

# #open and read the file after the appending:
# f = open("demo.txt", "r")
# print(f.read()) 

# f = open("demo.txt", "w") #Open the file "demo.txt" and overwrite the content:
# f.write("I have deleted the content")
# f.close()

# #open and read the file after the appending:
f = open("demo.txt", "r")
print(f.read())
f.close()

# f = open("myfile.txt", "w") # will create a file, returns an error if the file exist



