#Python program to find the sum of sequence of all numbers upto the given number using recursive function
def nat(num):
    if num<=1:
        return num
    else:
        return num+ nat(num-1)
list=[]
num=int(input("Enter the number"))
for n in range(num):
    list.append(n)
print(f"enter number is {num} ")
print(f"element is {list}")
print("sum is ",nat(num))


#Algoritham
#define a function def nat(num)
#check if num<=1
#then return num
#else,return num+nat(num-1)
#take a empty list 
#take input from user
#take a for loop
#put the number into the empty list
#print the number
#print list
#print sum