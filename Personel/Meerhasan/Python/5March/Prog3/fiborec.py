# 1. Take user input
# 2. Defining a function
# 3. Giving condition to the function
# 4. Return condition upto condition got failed 
# 5. Call the funtion and print 


def fibo(n):
    if n <= 1 :
        return n
    else:
        seq= fibo(n-1) + fibo(n-2)
        return seq
n = int(input("Enter number : "))
for i in range(n):
  print( fibo(i))

   