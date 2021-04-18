#sum od all numbers in list by using function :
def add():
    list=[1,2,3,4,5]
    print("Your list : ",list)
    b=len(list)
    i=0
    sum=0
    while i<b:

        sum=sum+(list[i])
        i+=1
    print("The sum of all numbers in list : ",sum)
add()

