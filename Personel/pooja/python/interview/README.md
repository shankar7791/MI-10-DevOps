# MI-10-DevOps
# MI-10-DevOps
MI-10 DevOps Internship Program

	1.sort list in ascending order?

numbers = [1, 3, 4, 2]
numbers.sort()
print(numbers)
******************************************************************************************************************
	Q 2 .File handling Operations?
* open file operation with the given example
file = open('geek.txt', 'r')
for each in file:
    print (each)
    
* read file operation
file = open("file.text", "r") 
print (file.read())

* write method
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

* delete a file

import os
os.remove(“demofile.txt”)

******************************************************************************************************
	Q 3 count number of vowels in string?
* prog:

string=raw_input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)
***************************************************************************************************************8
	Q4 Addition of the both list indices elements and store result in separate list?
test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]
 
print ("Original list 1 : " + str(test_list1))
print ("Original list 2 : " + str(test_list2))
   
res_list = [test_list1[i] + test_list2[i] for i in range(len(test_list1))]
  
print ("Resultant list is : " + str(res_list))
******************************************************************************************************************************
	Q5 Git Repository?
It contain collection of files and different versions of project.The process of copying the content from an existing Git Repository with the help of various Git Tools is termed as cloning.
***************************************************************************************************************************************************
	Q6 Git Commit?
In Git, commit is the term used for saving changes. Git does not add changes to a commit automatically. ... The commit command does not save changes in remote servers, only in the local repository of Git.
*****************************************************************************************************************************************
	Q7 write bubble sort program ?
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):           
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  arr = [64, 34, 25, 12, 22, 11, 90]
  
bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
  
for i in range(n-1):
arr = [64, 34, 25, 12, 22, 11, 90]
  
bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
*************************************************************************************************
	Q8 Database Queries?
1.  SELECT * FROM Customers;
2.  SELECT DISTINCT column1, column2, ...
	FROM table_name;	# distinct statement
3.  SELECT column1, column2, ...
    FROM table_name
    WHERE condition;    # where condition
4.  SELECT column1, column2, ...
	FROM table_name
	WHERE condition1 AND condition2 AND condition3 ...; # and syntax
5.  SELECT column1, column2, ...
	FROM table_name
	WHERE condition1 OR condition2 OR condition3 ...; #or syntax
6.  SELECT column1, column2, ...
	FROM table_name
	WHERE NOT condition; # not syntax
