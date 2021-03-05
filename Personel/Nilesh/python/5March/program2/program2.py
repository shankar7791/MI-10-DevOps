#Write a Python program to get the factorial of a number using recursion

#algorithm: 
#step 1: define the function and take 1 argument for which nos fact you want.
#step 2: check if that argument is equal to 1 return directly 1 as a fact.
        #step 1: otherwise go to else part for factorial formula and return the fact of that number.
#step 3: calling function and print the result.
#step 4: STOP
    


def factorial(n): 
 
   if n == 1:  
       return n  
   else:  
       return n*factorial(n-1)  

print(factorial(4))

