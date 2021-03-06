def r(k):
  if(k > 0):
    result = k + r(k - 1)
    print(k,"+",r(k-1),"=",result)
    print(result)
  else:
    result = 0
  return result
r(5)
 
        algo -
 
 step 1 - difine a function
 step 2 - check condition true than goto step 3 false than step6
 step 3 - result assign the opration recrsion function
 step 4 - print statement sequnce 
 step 5 - print  result 
 step 6 - else statement 
 step 7 - return of zero
 step 8 -out of function return result
 step 9 - calling function with parameter     
