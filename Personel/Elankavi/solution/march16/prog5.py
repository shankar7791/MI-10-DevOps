#Sum of all itemns in a dictionary :

def sum():
    dict={'a':20,'b':30,'c':40,'d':50}
    sum=0
    for i in dict:
        sum=sum+dict[i]
    print("The sum of all items  : ",sum)
sum()