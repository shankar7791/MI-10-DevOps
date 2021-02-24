num1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
x = 0 
y = 0
num = 0
while(num <len(num1)):
    if num1[num] % 2 == 0:
        x+=1
    else :
        y +=1
    num +=1
print("Number of even number : ", x)
print("Number of odd number : ", y)