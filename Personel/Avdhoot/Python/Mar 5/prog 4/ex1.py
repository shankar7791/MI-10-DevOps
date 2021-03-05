#Python program to find the sum of sequence of all numbers 
#upto the given number using recursive function

'''
Algorithm
1. Define a function
2. If num is 0 then return num and come outside the funtion
3. Used elif and num is 1 then return num and come outside the funtion
4. Write else + recursion
5. Take the user input and call the function and goto step 2
'''
def sum(num):
    if num == 0:
        return num
    elif num == 1:
        return num
    else :
        return num + sum(num - 1)

print(sum(int(input("Enter a Number: "))))