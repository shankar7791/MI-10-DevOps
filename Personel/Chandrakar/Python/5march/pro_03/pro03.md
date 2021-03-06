def r(n):  
   if n <= 1:  
       return n  
   else:  
       return(r(n-1) + r(n-2))  
num = 10
if num <= 0:  
   print()  
else:  
   print("Fibonacci sequence:")  
   for i in range(num):  
       print(r(i))  
       
       
           algo -
step 1 - difine  a function 
step 2 - check condition true than goto step 3 false than step4
step3 - return the n
step 4 - else statement
step 5 - return recrsion function
step 6 - assign the value
step 7 -  check condition true than goto step 8 false than step9
step 8 - print statement 
step 9 - else statement
step 10 - print statement
step 11 - for check the condition goto the step 12
step 12 - print and call function 
