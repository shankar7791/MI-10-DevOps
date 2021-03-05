
def sumR(list2):
    if len(list2)==0:
        return 0
    return list2[0]+sumR(list2[1:])    
print(sumR([10,20,30,40,50]))    

       algo-
       
  step1 - difine a  function
  step2 - check if condition true than goto step 3
  step3 - return statement  is zero
  step4 - out of if return opration function call and recursion process
  step5 - print statement and call the function      
