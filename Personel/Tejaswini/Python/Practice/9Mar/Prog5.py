
def findSum(str1):
    sum_digit = 0
    avg=0
    c=0
    for x in str1:
        if x.isdigit() == True:
            c = c+1
            z = int(x)
            sum_digit = sum_digit + z
    avg=sum_digit/c
    print("Average = ",avg)      
    return sum_digit
  
str1 = input("Enter the string : ")
print("Sum of digit : ",findSum(str1)) 

