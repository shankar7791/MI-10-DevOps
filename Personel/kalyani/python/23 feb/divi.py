# WAP to find those nos which are divisible by 7 and multiple by 5 betwwen 1500 and 2700

num = 1500
while num <= 2700 :
    num = num + 1
    if num%7==0 and num%5==0:
        print(num)