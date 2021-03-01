# Program to print even number using step size in range()
n = int(input("Enter the number : "))  
print("Even Numbers : ")
for i in range(2,n,2):  
    print(i)
else:
  print("Finally finished!\n") 
print("Odd Numbers : ")
for i in range(1,n,2):  
    print(i)
else:
  print("Finally finished!") 
