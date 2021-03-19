
# check student is pass or fail using array

import array as a 

per = a.array("i",[0,48,76,20,42,54,38,40,78,71])

n = int(input("Please Enter Your Roll No. => "))
print("Your Percentage is => ",per[n])

if per[n] > 30 :
    print("Congratulation!! You Passed The Exam ")

else :
    print("Unsuccessful")

