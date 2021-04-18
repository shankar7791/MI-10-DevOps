#Write a Python program to find a pair with highest product from a given array of integers.
"""Examples :
Input: arr[] = {1, 2, 3, 4, 7, 0, 8, 4}
Output: {7,8}
Input: arr[] = {0, -1, -2, -4, 5, 0, -6}
Output: {-4, -6}
"""

def max_num():

    Array=[]
    n=int(input("Enter Size of array : "))
    for x in range(0,n):
        a=int(input("Enter the element for array : "))
        Array.append(a)
    size=len(Array)
    a = Array[0] ; b = Array[1]
    if size<2:
        print("There is no pair of numbers")
    else:
        for i in range(0,n):
            for j in range(i+1,n):
                if Array[i] * Array[j] > a*b:
                    a=Array[i] ; b=Array[j]
    print("The maximum numbers are : ", a,b)
max_num()