# Program 8 : Write a Python program to create the multiplication table of a number. 
# Sample output :Input a number: 6 
# 6 x 1 = 6                                                              
# 6 x 2 = 12                                                             
# 6 x 3 = 18                                                             
# 6 x 4 = 24                                                             
# 6 x 5 = 30                                                             
# 6 x 6 = 36                                                             
# 6 x 7 = 42                                                             
# 6 x 8 = 48                                                             
# 6 x 9 = 54                                                             
# 6 x 10 = 60

a=int(input("Enter the table number : "))
i=1
while i<=10:
    print(a,"X",i,"=",a*i)
    i=i+1
