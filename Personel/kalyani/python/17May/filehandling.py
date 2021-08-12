file = open("file1.txt","w")
file.write("kalyani sandesh ruthwik rajkumar")
file.close()
file1 = open("file1.txt","r")
print("before sorting : ")
print(file1.read())
print("\n")
file1.close()

print("After sorting :")
def sorting(myfile):
  file_in = open(myfile)
  txt_file = []
  for line in file_in:
    data = line.split()

    for i in data:
      txt_file.append(i)
  file_in.close()
  txt_file.sort()
  file_out = open("file1.txt", "w")
  for i in txt_file:
    file_out.writelines(i)
    file_out.writelines(" ")
  file_out = open("file1.txt", "r")  
  print(file_out.read())  
  file_out.close()

sorting("file1.txt")