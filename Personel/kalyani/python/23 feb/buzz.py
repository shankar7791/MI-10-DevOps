# WAP to create the interger from 1 to 50. for multiple of 3 print 'fizz' 
# instead of the no anmd for the multiple of 5 print 'buzz' for nos which are multiple of both 3 and 5 'fizzbuzz'#

i = 1

while i <= 50 :

    if i % 15 == 0 :
    
         print("FizzBuzz ")
    elif  i % 3 == 0 :
         print("Fizz\t")
    elif  i % 5 == 0:
         print("Buzz\t")
    else :
         print(i)
         
    i=i+1