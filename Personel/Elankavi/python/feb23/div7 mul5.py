# program to find those number which are divisible by 7 and multiple by 5 between 1500 to 2700

i =1500
while (i>=1500):
    if(i % 7 ==0 ):
        print("The number divisible by 7 is : ",i)
    print("The multiple of 5 is : ",i*5)
    i=i+1
    if(i==2701):
        break