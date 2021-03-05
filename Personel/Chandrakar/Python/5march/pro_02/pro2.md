def fect_tori(fact):
    if fact == 1:
        return fact
    else :
        return fact*fect_tori(fact - 1)
num =5        
if num < 0 :
    print()
elif num ==0:
    print("fectorial is 1")    
else:
    print(fect_tori(num))
    
          algo -
          
step 1 - difine a function 
step 2 - check condition true than goto step 5 false than goto step4
step 3 - return statement 
step 4 - else statement
step 5 - return  function and opration
step 6 - assign the value
step 7 - out of function check condition true than goto step 8 false than step9
step 8 - check the condition  true than goto to step 9 
step 9 - print statement
step 10 - else statement 
step 11 - print and call the function
