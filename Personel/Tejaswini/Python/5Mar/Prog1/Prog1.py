#To calculate the sum of list of numbers using recursion

#Algorithm
#1. Take List and sun variable
#2. Define function 
#3. Call the function and pass List input as argument
#4. True condtion if length of list is equal to 1 then,
#   return 1st  element to function and goto step 5 otherwise, 
#   Flase condition: else return 1st element add  using recursivefun() goto step 2 upto last element 
#5. Print the result 

List=[1,2,3,51,10]
sum=0
def sumrev(List):
    if len(List)==1:
        return List[0]
    else:
        return List[0]+sumrev(List[1:])
    return sum
print("Sum of List of Element = ",sumrev(List))